import os
import pickle
import joblib
import librosa
import librosa.display
import numpy as np
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from matplotlib import pylab
from .models import TripleInputGenerator

le_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),f"weights/label_encoder/")
CUDA_VISIBLE_DEVICES = ""


def feature_extractor(row, nfft=2048, hoplen=512, nmels=224):
    audio, sr = librosa.load(row, res_type="kaiser_fast")
    # For MFCCS
    mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=39)
    mfccsscaled = np.mean(mfccs.T, axis=0)

    # Mel Spectogram imagepaths
    pylab.axis('off')  # no axis
    pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[])
    melspec = librosa.feature.melspectrogram(y=audio, sr=sr)
    s_db = librosa.power_to_db(melspec, ref=np.max)
    librosa.display.specshow(s_db)

    savepath = os.path.join(os.path.dirname(os.path.dirname(__file__)),f"weights/img_cough/current.png")
    pylab.savefig(savepath, bbox_inches=None, pad_inches=0)
    pylab.close()
    return mfccsscaled, savepath

def detect_cough(url_input):
  mf,mel = feature_extractor(url_input)
  mff=[mf]
  mell=[mel]
  labell=list([1])
  for i in range(598-1):
    mff.append(mf)
    mell.append(mel)
    labell.append(1)
  mfcc_test=np.array(mff)
  mel_test=np.array(mell)
  label_test=np.array(labell)
  test_model = keras.models.load_model(os.path.join(
      os.path.dirname(os.path.dirname(__file__)),
      f"weights/detect_model/test_model.h5"))
  pTEST = TripleInputGenerator(mfcc_test,mel_test,label_test,batch_size=48,target_size=(64,64))
  result = test_model.predict(pTEST)
  return result[0][0]

def get_metadata(dict_metadata):
    metadata_name = ["is_english_proficiency", "gender", "country", "locality", "state", "is_returning_user",
                     "is_smoker", "is_cold", "is_hypertension", "is_diabetes", "is_cough", "date_of_ct_scan","has_ctScan",
                     "ct_score", "is_diarrheoa", "is_fever", "is_loss_of_smell", "is_muscle_pain", "test_type",
                     "test_status", "is_using_mask", "vaccination_status", "is_breathing_difficulty", "is_others_resp",
                     "is_fatigue", "is_sore_throat", "is_ischemic_heart_disease", "is_asthma","is_others_preexist_conditions",
                     "is_chronic_lung_disease", "is_neumonia", "age", "latitude", "longitude", "respiratory_condition",
                     "fever_muscle_pain", "status", "quality_1", "cough_type_1", "dyspnea_1", "wheezing_1", "stridor_1",
                     "choking_1", "congestion_1", "nothing_1", "diagnosis_1", "severity_1", "quality_2", "cough_type_2",
                     "dyspnea_2", "wheezing_2", "stridor_2", "choking_2", "congestion_2", "nothing_2", "diagnosis_2",
                     "severity_2", "quality_3", "dyspnea_3", "wheezing_3", "stridor_3", "choking_3", "congestion_3",
                     "nothing_3", "cough_type_3", "diagnosis_3", "severity_3", "subject_gender", "subject_age","num_chunk"]
    metadata = {}
    for name in metadata_name:
        metadata[name] = "unknown"
        for key,value in dict_metadata.items():
            #print(key,": ",value)
            if str(key) == name:
                metadata[name] = value
                #print(name,": ",value)
    metadata['subject_gender']=metadata['gender']
    metadata['subject_age']=metadata['age']
    return metadata

def label_encoding(metadata, path, model_name):
    # INPUT: METADATA FEATURES, MODEL_NAME, path LE
    # OUTPUT: TRANSFORMED FEATURES
    data = ['aicovidvn', 'coswara', 'coughvid']
    typ = ['chunk', 'full']
    X = []
    for a in data:
        for b in typ:
            if (a in model_name) and (b in model_name):
                for name, mdata in metadata.items():
                    try:
                        le = pickle.load(open(path + "les_" + a + "_" + b + "_" + name + ".pkl", 'rb'))
                        try:
                            x = le.transform([mdata])
                        except:
                            x = np.array([0])
                        X.append(x)
                    except:
                        continue
    # Reshape X-1D
    f1 = np.array(X)
    f1 = f1[None, ...]
    return f1

def lengthen_cough(data: np.array, n):
  temp = data
  for i in range(n-1):
    temp = np.concatenate([temp, data])
  return temp

def extract(path, nfft=2048, hoplen=512, nmels=224):
    START_SAMPLE = 10000
    SAMPLES_TO_CONSIDER_FULL = 135440 # 5 seconcs
    SAMPLES_TO_CONSIDER_CHUNK = 22050

    data_raw, sample_rate = librosa.load(path, res_type="kaiser_fast")
        #FULL COUGH
    data = librosa.util.fix_length(data_raw, SAMPLES_TO_CONSIDER_FULL) # take 5 seconds
    data = data[START_SAMPLE:]

    mel_spec = librosa.feature.melspectrogram(y=data,
                                            sr=sample_rate,
                                            n_fft=nfft,
                                            hop_length=hoplen,
                                            n_mels=nmels)
    log_mel_spec = librosa.power_to_db(mel_spec)

    mfcc = []
    for i in range(3):
          mfcc_i = librosa.feature.mfcc(y=data,
                                  sr=sample_rate,
                                  n_fft=nfft,
                                  hop_length=hoplen,
                                  n_mfcc=13*(i+1))
          mfcc.append(mfcc_i)

    mel, mfcc_13, mfcc_26, mfcc_39 = log_mel_spec, lengthen_cough(mfcc[0], int(nmels/13)+1), lengthen_cough(mfcc[1], int(nmels/26)+1), lengthen_cough(mfcc[2], int(nmels/39)+1)

        #CHUNK COUGH
    data = data_raw[START_SAMPLE:SAMPLES_TO_CONSIDER_CHUNK]
    long_data = lengthen_cough(data, 10)

    mel_spec = librosa.feature.melspectrogram(y=long_data,
                                            sr=sample_rate,
                                            n_fft=nfft,
                                            hop_length=hoplen,
                                            n_mels=nmels)
    log_mel_spec = librosa.power_to_db(mel_spec)

    mfcc = []
    for i in range(3):
          mfcc_i = librosa.feature.mfcc(y=long_data,
                                  sr=sample_rate,
                                  n_fft=nfft,
                                  hop_length=hoplen,
                                  n_mfcc=13*(i+1))
          mfcc.append(mfcc_i)

    mel_chunk, mfcc_13_chunk, mfcc_26_chunk, mfcc_39_chunk = log_mel_spec, lengthen_cough(mfcc[0], int(nmels/13)+1), lengthen_cough(mfcc[1], int(nmels/26)+1), lengthen_cough(mfcc[2], int(nmels/39)+1)

    return {'mel':mel,'mel_chunk':mel_chunk,'mfcc_13':mfcc_13,'mfcc_13_chunk':mfcc_13_chunk,'mfcc_26':mfcc_26,'mfcc_26_chunk':mfcc_26_chunk,'mfcc_39':mfcc_39,'mfcc_39_chunk':mfcc_39_chunk}

def def_shape(data):
    data = data[..., np.newaxis]
    data = data[np.newaxis, ...]
    return data

def scaler(data,name):
    dataset = ['aicovidvn','coswara','coughvid']
    model = ['hybrid','mobilenet']
    feat = ['mel','mfcc_13','mfcc_26','mfcc_39']
    typ = ['chunk_cough','full_cough']
    scaler_name = ''
    for a in dataset:
        for b in model:
            for c in feat:
                for d in typ:
                    if (a in name) and (b in name) and (c in name) and (d in name):
                        scaler_name = d+'_'+b+'_'+a+'_'+c+'_standard_scaler'
    scaler = pickle.load(open(os.path.join(
                        os.path.dirname(os.path.dirname(__file__)),
                        f"weights/scalers/{scaler_name}.pkl"),"rb"))

    return scaler.transform(data)

def predict(file,metadata):
    model_list = os.listdir(os.path.join(os.path.dirname(os.path.dirname(__file__)),f"weights/models/"))
    features = extract(file)

    res,sample_number = 0,0
    for name in model_list:
        print('MODEL: ', name)

        for feat in ['mel','mfcc_13','mfcc_26','mfcc_39']:
            if feat in name:
                if "chunk" in name:
                    x = features[feat+"_chunk"]
                else:
                    x = features[feat]
                if 'std' in name:
                    x = scaler(x, str(name))
                x = def_shape(x)
                break
        if 'hybrid' in name:
            #metadata = get_metadata()
            x_meta = label_encoding(metadata,le_path,name)
            x = [x,x_meta]

        model = keras.models.load_model(os.path.join(
                                    os.path.dirname(os.path.dirname(__file__)),
                                    f"weights/models/" + name))
        score = model.predict(x)
        if ("smote" in name):
            temp = score[0][0]
            score[0][0]=score[0][1]
            score[0][1]=temp
        print("SCORE: ",score)
        res += score#model.predict(x)
        #sample_number = sample_number+1
    return (res /len(model_list))[0]#(res /sample_number)[0]
