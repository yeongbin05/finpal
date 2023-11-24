<template>
  <div>
    <div v-if="language==='한국어'">
    <h2 style="margin-left : 300px; ">카카오 맵 보기</h2>
  </div>
  <div v-else>
    
    <h2 style="margin-left : 300px; ">Map</h2>
  </div>
  
    <!-- <div>선택됨: {{ selected_seoul }}</div>
    <select v-model="selected_seoul">
    <option v-for="option1 in options_seoul" :key="option1" :value="option1.value">
      {{ option1.text }}
    </option>
  </select> -->
  
  <!-- <select v-model="selected_si">
    <option v-for="option2 in options_si" :key="option2" :value="option2.value">
      {{ option2.text }}
    </option>
  </select>
  <div>선택됨: {{ selected_si }}</div>
  
    <div id="map"></div>
  </div> -->
  
  <!-- <form class='map-forms' @submit.prevent="searchPlace(selected1+' '+selected2+' '+selected3)">
      <div> -->
      <!-- <label for="도">시/군</label> -->
      <!-- <input type="search" v-model="selected1" placeholder="시/군">
    </div>
    <div> -->
      <!-- <label for="시/군">구</label> -->
      <!-- <input type="search" v-model="selected2" @change="onSelected2Change" placeholder="구">
    </div>
    <div>
      <label for="은행">은행</label>
      <input type="search" v-model="selected3" @change="onSelected3Change" placeholder="은행">
    </div>
      <input type="submit" value="찾기">
    </form> -->
  
    <div>
    <div>
    <!-- Your other template code here -->

    <div class="select-div">
    <div v-for="code in sidolist" :key="code.id">
      <!-- <p>{{ code[0].name }}</p> -->
      <!-- <label for="sidoselect">Choose an option:</label> -->
      <select v-model="selectedCode1" @change="onSelected2Change" id="sidoselect">
        <option disabled selected value="">시/도를 선택해주세요.</option>
        <option v-for="optionCode in code" :key="optionCode.id" :value="optionCode">
          {{ optionCode.name }}
        </option>
      </select>
    </div>

    <div v-for="code in sigungulist" :key="code.id">
      <!-- <p>{{ code[0].name }}</p> -->
      <!-- <label for="sigunguselect">Choose an option:</label> -->
      <select v-model="selectedCode2" @change="onSelected3Change" id="sigunguselect">
        <option disabled selected value="">시/군/구를 선택해주세요.</option>
        <option v-for="optionCode in code" :key="optionCode.id" :value="optionCode">
          {{ optionCode.name }}
        </option>
      </select>
    </div>

    <div v-for="code in donglist" :key="code.id">
      <!-- <p>{{ code[0].name }}</p> -->
      <!-- <label for="dongselect">Choose an option:</label> -->
      <select v-model="selectedCode3"  id="dongselect">
        <option disabled selected value="">읍/면/동/리를 선택해주세요.</option>
        <option v-for="optionCode in code" :key="optionCode.id" :value="optionCode">
          {{ optionCode.name }}
        </option>
      </select>
    </div>
    <br>
     <!-- Display the selected code -->
    <!-- <p>Selected Code: {{ selectedCode ? selectedCode.name : 'None' }}</p> -->
  </div>

  </div>
</div>
  
  <div id="map" style="width:80%;height:350px; margin : auto;"></div>
  </div>
  </template>
  
  <style scoped>
  input {
    margin-right : 10px;
  }
  #map {
  width: 100%;
  height: 400px;
  }
  .map-forms {
    display : flex;
    margin-bottom : 10px;
    justify-content: center;
  }
  </style>
    <script setup>
    import { ref,inject } from 'vue'
    import axios from 'axios'
   
  </script>
    <script >
    import { ref,inject } from 'vue'
    const language = inject('language',ref(''))
    console.log(language)
  
  export default {
  name: "KakaoMap", // 컴포넌트 이름 지정
  data() {
    return {
      selected1: '',
      selected2: '',
      selected3: '',
      sidolist: [],
      sigungulist: [],
      donglist: [],
      selectedCode1: 11,
      selectedCode2: null,
      selectedCode3: null,
      // map 객체 설정
      // map: null,
    };
  },
  mounted() {
      // api 스크립트 소스 불러오기 및 지도 출력
    if (window.kakao && window.kakao.maps) {
      this.loadMap();
    } else {
      this.loadScript();
    }
    this.sidoCodes();
    this.sigunguCodes();
    this.dongCodes();
  },
  methods: {
      // api 불러오기

       // api 불러오기

       onSelected2Change() {
      // 이 메서드에서 select가 변경됐을 때 실행할 로직을 추가하세요.
      // 예를 들어, sigunguCodes()를 호출하거나 다른 로직을 추가할 수 있습니다.
      this.sigunguCodes();
      },

      onSelected3Change() {
        // 이 메서드에서 select가 변경됐을 때 실행할 로직을 추가하세요.
        // 예를 들어, sigunguCodes()를 호출하거나 다른 로직을 추가할 수 있습니다.
        this.dongCodes();
      },

      sidoCodes() {
        axios({
          method: 'get',
          url: `https://grpc-proxy-server-mkvo6j4wsq-du.a.run.app/v1/regcodes?regcode_pattern=*00000000`
        })
        .then((res) => {
          this.sidolist = res.data;
          console.log(res.data)
        })
        .catch((error) => {
          console.error("API 호출 중 에러 발생:", error);
        })
      },
      
      sigunguCodes() {
        if (this.selectedCode1 && this.selectedCode1.code) {
            // Use substring only if selectedCode1 and its code property exist
            var tempcode1 = this.selectedCode1.code.substring(0, 2);

      axios({
        method: 'get',
        url: `https://grpc-proxy-server-mkvo6j4wsq-du.a.run.app/v1/regcodes?regcode_pattern=${tempcode1}???00000`
        })
        .then((res) => {
        this.sigungulist = res.data;
        console.log(tempcode1)
        console.log(res.data)
        })
        .catch((error) => {
        console.error("API 호출 중 에러 발생:", error);
        }) } else {
        console.error("selectedCode1 is null or undefined");
      }
      },

      dongCodes() {
        if (this.selectedCode1 && this.selectedCode1.code) {
            // Use substring only if selectedCode1 and its code property exist
            var tempcode1 = this.selectedCode2.code.substring(0, 5);

      axios({
      method: 'get',
        url: `https://grpc-proxy-server-mkvo6j4wsq-du.a.run.app/v1/regcodes?regcode_pattern=${tempcode1}*`
        })
        .then((res) => {
        this.donglist = res.data;
        console.log(res.data)
        console.log(tempcode1)
        })
        .catch((error) => {
        console.error("API 호출 중 에러 발생:", error);
      })
    }
    }, 

    loadScript() {
      const script = document.createElement("script");
      script.src =
        // "//dapi.kakao.com/v2/maps/sdk.js?appkey=b63dd7cc18d4a3f04b7d7d4d212ffc38&libraries=services&autoload=false"; 
        "//dapi.kakao.com/v2/maps/sdk.js?appkey=446b7caced64ca3ed637bd373f449f42&libraries=services&autoload=false"; 
      script.onload = () => window.kakao.maps.load(this.loadMap); 
      document.head.appendChild(script);
    },
    // 맵 출력하기(현재 설정해둔 위치-역삼역)
    loadMap() {
      const container = document.getElementById("map"); 
      const options = {
        center: new window.kakao.maps.LatLng(37.49982193285956, 127.03690105516682), 
        level: 3
      };
  
      var map = new window.kakao.maps.Map(container, options);
  
      // 초기에 설정해둔 지도의 중심좌표를 마커로 표시할 거임.
      var marker = new window.kakao.maps.Marker({
        position: map.getCenter() // 지도의 중심좌표
      })
      marker.setMap(map)
    },
  
    // 키워드로 장소 서치할 거임
    searchPlace() {
  
      const mapContainer = document.getElementById("map"); 
      const mapOptions = {
        center: new window.kakao.maps.LatLng(37.49982193285956, 127.03690105516682), 
        level: 3
      };
  
      var map = new window.kakao.maps.Map(mapContainer, mapOptions);
  
  
      const keyword = `${this.selected1} ${this.selected2} ${this.selected3}`;
      if (keyword.length === 0) {
        return;
      }
      const ps = new window.kakao.maps.services.Places();
      ps.keywordSearch(keyword, placesSearchCB)
  
  
      function placesSearchCB (data, status, pagination) {
        // console.log(data)
        if (status === kakao.maps.services.Status.OK) {
          // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
          // LatLngBounds 객체에 좌표를 추가합니다
          loadMaker(data);
        }
      }
  
      // 지정한 위치에 마커 불러오기
      function loadMaker(places) {
      
        console.log(places)
        var infowindow = new kakao.maps.InfoWindow({zIndex:1});
        var bounds = new window.kakao.maps.LatLngBounds()
        for (let i = 0; i < places.length; i++) {
          var markerPosition = new window.kakao.maps.LatLng(
            places[i].y,
            places[i].x
          );
          const marker = new window.kakao.maps.Marker({
          position: markerPosition,
          });
          marker.setMap(map);
  
          bounds.extend(markerPosition);
          // 마커에 클릭이벤트를 등록합니다
          window.kakao.maps.event.addListener(marker, 'click', function() {
          // 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
          console.log(places[i])
          infowindow.setContent('<div style="padding:5px;font-size:12px;">' + places[i].place_name + '</div>');
    
          // console.log(ma rker)
          infowindow.open(map, marker);
          });
  
          // console.log(infowindow.open(this.map, marker))
  
          map.setBounds(bounds)
        }
  
  
        }
  }
  }
  };
  </script>

  <style scoped>
.select-div {
  display: flex;
  margin-bottom: 30px;
}

</style>