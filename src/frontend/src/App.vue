<template>
  <div class="page-loader" v-if="!isLoaded">
    <div style="background-color: #8cc271" class="cube first"></div>
    <div style="background-color: #69beeb" class="cube"></div>
    <div style="background-color: #f5aa39" class="cube"></div>
    <div style="background-color: #e9643b" class="cube last"></div>
  </div>
  <div id="head">
      <img id="logouit" src="./assets/uit.png">
      <p>Đề tài tốt nghiệp: Nhận diện Covid-19 qua tiếng ho <a target="_blank" style="color: #004fcf;" href="https://github.com/dee-ex/aicovidvn115m">[Github]</a></p>
  </div>

  <div>
        <p id="head_1">Metadata User</p>
        <table id="left_2">
          <tr>
            <th></th>
            <th></th>
            <th></th>
            <th></th>
            <th></th>
          </tr>

          <tr>
            <td>locality :  <input type="text" name=" locality " v-model=" locality "><br>
                date_of_ct_scan :  <input type="text" name=" date_of_ct_scan " v-model=" date_of_ct_scan "><br>
                has_ctScan :  <input type="text" name=" has_ctScan " v-model=" has_ctScan "><br>
                ct_score :  <input type="text" name=" ct_score " v-model=" ct_score "><br>
                test_type :  <input type="text" name=" test_type " v-model=" test_type "><br>
                test_status :  <input type="text" name=" test_status " v-model=" test_status "><br>
                vaccination_status :  <input type="text" name=" vaccination_status " v-model=" vaccination_status "><br>
                respiratory_condition :  <input type="text" name=" respiratory_condition " v-model=" respiratory_condition "><br>
                fever_muscle_pain :  <input type="text" name=" fever_muscle_pain " v-model=" fever_muscle_pain "><br>
                is_english_proficiency :  <input type="text" name=" is_english_proficiency " v-model=" is_english_proficiency "><br>
                is_returning_user :  <input type="text" name=" is_returning_user " v-model=" is_returning_user "><br>
                is_smoker :  <input type="text" name=" is_smoker " v-model=" is_smoker "><br>

            </td>

            <td>country :  <input type="text" name=" country " v-model=" country "><br>
                state :  <input type="text" name=" state " v-model=" state "><br>
                latitude :  <input type="text" name=" latitude " v-model=" latitude "><br>
                longitude :  <input type="text" name=" longitude " v-model=" longitude "><br>
                quality_1 :  <input type="text" name=" quality_1 " v-model=" quality_1 "><br>
                cough_type_1 :  <input type="text" name=" cough_type_1 " v-model=" cough_type_1 "><br>
                dyspnea_1 :  <input type="text" name=" dyspnea_1 " v-model=" dyspnea_1 "><br>
                wheezing_1 :  <input type="text" name=" wheezing_1 " v-model=" wheezing_1 "><br>
                stridor_1 :  <input type="text" name=" stridor_1 " v-model=" stridor_1 "><br>
                choking_1 :  <input type="text" name=" choking_1 " v-model=" choking_1 "><br>
                congestion_1 :  <input type="text" name=" congestion_1 " v-model=" congestion_1 "><br>
                nothing_1 :  <input type="text" name=" nothing_1 " v-model=" nothing_1 "><br>
                diagnosis_1 :  <input type="text" name=" diagnosis_1 " v-model=" diagnosis_1 "><br>
                severity_1 :  <input type="text" name=" severity_1 " v-model=" severity_1 "><br>
            </td>

            <td>age :  <input type="text" name=" age " v-model=" age "><br>
                gender :  <input type="text" name=" gender " v-model=" gender "><br>
                status :  <input type="text" name=" status " v-model=" status "><br>
                cough_type_2 :  <input type="text" name=" cough_type_2 " v-model=" cough_type_2 "><br>
                dyspnea_2 :  <input type="text" name=" dyspnea_2 " v-model=" dyspnea_2 "><br>
                wheezing_2 :  <input type="text" name=" wheezing_2 " v-model=" wheezing_2 "><br>
                stridor_2 :  <input type="text" name=" stridor_2 " v-model=" stridor_2 "><br>
                choking_2 :  <input type="text" name=" choking_2 " v-model=" choking_2 "><br>
                congestion_2 :  <input type="text" name=" congestion_2 " v-model=" congestion_2 "><br>
                nothing_2 :  <input type="text" name=" nothing_2 " v-model=" nothing_2 "><br>
                diagnosis_2 :  <input type="text" name=" diagnosis_2 " v-model=" diagnosis_2 "><br>
                severity_2 :  <input type="text" name=" severity_2 " v-model=" severity_2 "><br>
                quality_2 :  <input type="text" name=" quality_2 " v-model=" quality_2 "><br>

            </td>

            <td>
                is_cold :  <input type="text" name=" is_cold " v-model=" is_cold "><br>
                is_hypertension :  <input type="text" name=" is_hypertension " v-model=" is_hypertension "><br>
                is_diabetes :  <input type="text" name=" is_diabetes " v-model=" is_diabetes "><br>
                is_cough :  <input type="text" name=" is_cough " v-model=" is_cough "><br>
                is_diarrheoa :  <input type="text" name=" is_diarrheoa " v-model=" is_diarrheoa "><br>
                is_fever :  <input type="text" name=" is_fever " v-model=" is_fever "><br>
                is_loss_of_smell :  <input type="text" name=" is_loss_of_smell " v-model=" is_loss_of_smell "><br>
                is_muscle_pain :  <input type="text" name=" is_muscle_pain " v-model=" is_muscle_pain "><br>
                is_breathing_difficulty :  <input type="text" name=" is_breathing_difficulty " v-model=" is_breathing_difficulty "><br>
                is_others_resp :  <input type="text" name=" is_others_resp " v-model=" is_others_resp "><br>
                is_fatigue :  <input type="text" name=" is_fatigue " v-model=" is_fatigue "><br>
                is_sore_throat :  <input type="text" name=" is_sore_throat " v-model=" is_sore_throat "><br>
                is_ischemic_heart_disease :  <input type="text" name=" is_ischemic_heart_disease " v-model=" is_ischemic_heart_disease "><br>
                is_asthma :  <input type="text" name=" is_asthma " v-model=" is_asthma "><br>

            </td>

            <td>
                is_others_preexist_conditions :  <input type="text" name=" is_others_preexist_conditions " v-model=" is_others_preexist_conditions "><br>
                is_chronic_lung_disease :  <input type="text" name=" is_chronic_lung_disease " v-model=" is_chronic_lung_disease "><br>
                is_neumonia :  <input type="text" name=" is_neumonia " v-model=" is_neumonia "><br>
                is_using_mask :  <input type="text" name=" is_using_mask " v-model=" is_using_mask "><br>
                quality_3 :  <input type="text" name=" quality_3 " v-model=" quality_3 "><br>
                dyspnea_3 :  <input type="text" name=" dyspnea_3 " v-model=" dyspnea_3 "><br>
                wheezing_3 :  <input type="text" name=" wheezing_3 " v-model=" wheezing_3 "><br>
                stridor_3 :  <input type="text" name=" stridor_3 " v-model=" stridor_3 "><br>
                choking_3 :  <input type="text" name=" choking_3 " v-model=" choking_3 "><br>
                congestion_3 :  <input type="text" name=" congestion_3 " v-model=" congestion_3 "><br>
                nothing_3 :  <input type="text" name=" nothing_3 " v-model=" nothing_3 "><br>
                cough_type_3 :  <input type="text" name=" cough_type_3 " v-model=" cough_type_3 "><br>
                diagnosis_3 :  <input type="text" name=" diagnosis_3 " v-model=" diagnosis_3 "><br>
                severity_3 :  <input type="text" name=" severity_3 " v-model=" severity_3 "><br>
            </td>

            <td>
            </td>

          </tr>
        </table>

  </div>

  <div id="up" class ="terms_1">
    <button id="button" onclick="document.getElementById('inputfile').click()">CHỌN FILE</button>
    <input type='file' id="inputfile" style="display:none" @change="onFileChange">
    <button id="process" @click="onProcess">DỰ ĐOÁN</button>
  </div>

  <div id="down">
      <div id="left">
        <audio controls v-if="url" :key="url">
          <source :src="url" alt="file đầu vào" type="audio/wav">
        </audio>
      </div>
      <div id="right">
        <h2 style="color: white">
          Xác suất dương tính là:
          <span v-if="res" v-bind:class="{low: low, low_mid: low_mid, mid: mid, mid_high: mid_high, high: high}">{{ res }}</span>
        </h2>
      </div>
  </div>
  <footer>	<p><b>SVTH</b>: Dương Văn Bình - Lê Trần Hoài Ân</p>
			<p><b>GVHD</b>: TS. Đỗ Trọng Hợp</p>
  </footer>
</template>

<script>

export default {
  name: 'App',
  data() {
    return {
      isLoaded: false,
      file: null,
      url: null,
      res: null,
      fd: null,
      low: null,
      low_mid: null,
      mid: null,
      mid_high: null,
      high: null,

        age: 'unknown',
        is_english_proficiency : 'unknown',
        gender : 'unknown',
        country : 'unknown',
        locality : 'unknown',
        state : 'unknown',
        is_returning_user : 'unknown',
        is_smoker : 'unknown',
        is_cold : 'unknown',
        is_hypertension : 'unknown',
        is_diabetes : 'unknown',
        is_cough : 'unknown',
        date_of_ct_scan : 'unknown',
        has_ctScan : 'unknown',
        ct_score : 'unknown',
        is_diarrheoa : 'unknown',
        is_fever : 'unknown',
        is_loss_of_smell : 'unknown',
        is_muscle_pain : 'unknown',
        test_type : 'unknown',
        test_status : 'unknown',
        is_using_mask : 'unknown',
        vaccination_status : 'unknown',
        is_breathing_difficulty : 'unknown',
        is_others_resp : 'unknown',
        is_fatigue : 'unknown',
        is_sore_throat : 'unknown',
        is_ischemic_heart_disease : 'unknown',
        is_asthma : 'unknown',
        is_others_preexist_conditions : 'unknown',
        is_chronic_lung_disease : 'unknown',
        is_neumonia : 'unknown',
        latitude : 'unknown',
        longitude : 'unknown',
        respiratory_condition : 'unknown',
        fever_muscle_pain : 'unknown',
        status : 'unknown',
        quality_1 : 'unknown',
        cough_type_1 : 'unknown',
        dyspnea_1 : 'unknown',
        wheezing_1 : 'unknown',
        stridor_1 : 'unknown',
        choking_1 : 'unknown',
        congestion_1 : 'unknown',
        nothing_1 : 'unknown',
        diagnosis_1 : 'unknown',
        severity_1 : 'unknown',
        quality_2 : 'unknown',
        cough_type_2 : 'unknown',
        dyspnea_2 : 'unknown',
        wheezing_2 : 'unknown',
        stridor_2 : 'unknown',
        choking_2 : 'unknown',
        congestion_2 : 'unknown',
        nothing_2 : 'unknown',
        diagnosis_2 : 'unknown',
        severity_2 : 'unknown',
        quality_3 : 'unknown',
        dyspnea_3 : 'unknown',
        wheezing_3 : 'unknown',
        stridor_3 : 'unknown',
        choking_3 : 'unknown',
        congestion_3 : 'unknown',
        nothing_3 : 'unknown',
        cough_type_3 : 'unknown',
        diagnosis_3 : 'unknown',
        severity_3 : 'unknown',
        num_chunk : 'unknown',
    }
  },
  mounted() {
    document.onreadystatechange = () => {
      if (document.readyState == "complete") {
        this.isLoaded = true;
      }
    }
  },
  methods: {
    onFileChange(e) {
      this.file = e.target.files[0];
      console.log(this.file);
      this.url = URL.createObjectURL(this.file);
    },
    onProcess() {
      this.isLoaded = false;

      this.fd = new FormData();
        this.fd.append("url",this.url);
        this.fd.append("is_english_proficiency", this.is_english_proficiency);
        this.fd.append("gender", this.gender);
        this.fd.append("country", this.country);
        this.fd.append("locality", this.locality);
        this.fd.append("state", this.state);
        this.fd.append("is_returning_user", this.is_returning_user);
        this.fd.append("is_smoker", this.is_smoker);
        this.fd.append("is_cold", this.is_cold);
        this.fd.append("is_hypertension", this.is_hypertension);
        this.fd.append("is_diabetes", this.is_diabetes);
        this.fd.append("is_cough", this.is_cough);
        this.fd.append("date_of_ct_scan", this.date_of_ct_scan);
        this.fd.append("has_ctScan", this.has_ctScan);
        this.fd.append("ct_score", this.ct_score);
        this.fd.append("is_diarrheoa", this.is_diarrheoa);
        this.fd.append("is_fever", this.is_fever);
        this.fd.append("is_loss_of_smell", this.is_loss_of_smell);
        this.fd.append("is_muscle_pain", this.is_muscle_pain);
        this.fd.append("test_type", this.test_type);
        this.fd.append("test_status", this.test_status);
        this.fd.append("is_using_mask", this.is_using_mask);
        this.fd.append("vaccination_status", this.vaccination_status);
        this.fd.append("is_breathing_difficulty", this.is_breathing_difficulty);
        this.fd.append("is_others_resp", this.is_others_resp);
        this.fd.append("is_fatigue", this.is_fatigue);
        this.fd.append("is_sore_throat", this.is_sore_throat);
        this.fd.append("is_ischemic_heart_disease", this.is_ischemic_heart_disease);
        this.fd.append("is_asthma", this.is_asthma);
        this.fd.append("is_others_preexist_conditions", this.is_others_preexist_conditions);
        this.fd.append("is_chronic_lung_disease", this.is_chronic_lung_disease);
        this.fd.append("is_neumonia", this.is_neumonia);
        this.fd.append("age", this.age);
        this.fd.append("latitude", this.latitude);
        this.fd.append("longitude", this.longitude);
        this.fd.append("respiratory_condition", this.respiratory_condition);
        this.fd.append("fever_muscle_pain", this.fever_muscle_pain);
        this.fd.append("status", this.status);
        this.fd.append("quality_1", this.quality_1);
        this.fd.append("cough_type_1", this.cough_type_1);
        this.fd.append("dyspnea_1", this.dyspnea_1);
        this.fd.append("wheezing_1", this.wheezing_1);
        this.fd.append("stridor_1", this.stridor_1);
        this.fd.append("choking_1", this.choking_1);
        this.fd.append("congestion_1", this.congestion_1);
        this.fd.append("nothing_1", this.nothing_1);
        this.fd.append("diagnosis_1", this.diagnosis_1);
        this.fd.append("severity_1", this.severity_1);
        this.fd.append("quality_2", this.quality_2);
        this.fd.append("cough_type_2", this.cough_type_2);
        this.fd.append("dyspnea_2", this.dyspnea_2);
        this.fd.append("wheezing_2", this.wheezing_2);
        this.fd.append("stridor_2", this.stridor_2);
        this.fd.append("choking_2", this.choking_2);
        this.fd.append("congestion_2", this.congestion_2);
        this.fd.append("nothing_2", this.nothing_2);
        this.fd.append("diagnosis_2", this.diagnosis_2);
        this.fd.append("severity_2", this.severity_2);
        this.fd.append("quality_3", this.quality_3);
        this.fd.append("dyspnea_3", this.dyspnea_3);
        this.fd.append("wheezing_3", this.wheezing_3);
        this.fd.append("stridor_3", this.stridor_3);
        this.fd.append("choking_3", this.choking_3);
        this.fd.append("congestion_3", this.congestion_3);
        this.fd.append("nothing_3", this.nothing_3);
        this.fd.append("cough_type_3", this.cough_type_3);
        this.fd.append("diagnosis_3", this.diagnosis_3);
        this.fd.append("severity_3", this.severity_3);
        this.fd.append("num_chunk", this.num_chunk);
        this.fd.append("audio_1", this.file);
      this.fd.append("audio", this.file);

      fetch("http://localhost:8000/api/predict/", {method: "POST", body: this.fd})
      .then(response => response.json())
      .then(data => {
        this.res = data["prob"]
        if (.3 - this.res >= 1e-9) {
          this.low = true;
          this.low_mid = false
          this.mid = false;
          this.mid_high = false;
          this.high = false
        } else if (.5 - this.res > 1e-9) {
          this.low = false;
          this.low_mid = true;
          this.mid = false;
          this.mid_high = false;
          this.high = false;
        } 
        else if (.7 - this.res >= 1e-9) {
          this.low = false;
          this.low_mid = false;
          this.mid = true;
          this.mid_high = false;
          this.high = false;
        } else if (.8 - this.res >= 1e-9) {
          this.low = false;
          this.low_mid = false;
          this.mid = false;
          this.mid_high = true
          this.high = false;
        } else {
          this.low = false;
          this.low_mid = false;
          this.mid = false;
          this.mid_high = false;
          this.high = true;
        }

        this.isLoaded = true;
      });
    },
  },
}
</script>

<style>

@keyframes left {
  40% {
    transform: translateX(-60px);
  }

  50% {
    transform: translateX(0);
  }
}

@keyframes right {
  40% {
    transform: translateX(60px);
  }

  50% {
    transform: translateX(0);
  }
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  padding-left: 10%;
  padding-right: 10%;
}

div {
  border-radius: 12px;
}

.page-loader {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(3, 3, 3, .3);
  z-index: 999;
}

.cube {
  width: 40px;
  height: 40px;
  margin-right: 10px;
}

.first {
  animation: left 1s infinite;
}

.last {
  animation: right 1s infinite .5s;
}

#head {
    padding: 10px;
    text-align: center;
    background-color: #ffa263;
    font-size: 30px;
    font-weight: bold;
    color: blue;
    margin: 1%;
}
#head_1 {
    padding: 10px;
    text-align: center;
    font-size: 20px;
    font-weight: bold;
    color: black;
    margin: .1%;
}

#up {
    padding: 10px 10px;
    margin: 1%;
    padding-left: 39%;
}

#logohcmut {
    width: 50%;
    height: 50%;
    cursor: pointer;
}

#logouit {
    width: 60%;
    height: 60%;
    cursor: pointer;
}

#button {
    display: block;
    background-color: white;
    border: 2px solid #074B80;
    color: black;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    border-radius: 12px;
    margin-right: 10px;
}

#process {
    display: block;
    background-color: white;
    border: 2px solid #4CAF50;
    color: black;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    border-radius: 12px;
}

#button:hover {
    background-color: #074B80;
    color: white;
    cursor: pointer;
}

#process:hover {
    background-color: #4CAF50;
    color: white;
    cursor: pointer;
}

#left {
    float: left;
    background: gray;
    width: 48%;
    height: 200px;
    margin: 1%;
    display: flex;
    align-items: center;
    justify-content: center;
}

#right {
    float: right;
    background: gray;
    width: 48%;
    height: 200px;
    margin: 1%;
    display: flex;
    align-items: center;
    justify-content: center;
}

#left_2 {
    float: left;
    background: gray;
    width: 100%;
    height: 600px;
    display: flex;
    margin: 1%;
    align-items: left;
    justify-content: left;
}


.low {
    color: #00ff55;
    display: block;
    margin: 10px 10px;
}

.low_mid {
    color: #66f706;
    display: block;
    margin: 10px 10px;
}

.mid {
    color: #fffb00;
    display: block;
    margin: 10px 10px;
}

.mid_high {
    color: #ff7b00;
    display: block;
    margin: 10px 10px;
}

.high {
    color: #ff0000;
    display: block;
    margin: 10px 10px;
}

footer {
    margin: 1%;
    text-align: left;
    color: #074B80;
    font-size: 15px;
    margin-top: 8%;
}
</style>
