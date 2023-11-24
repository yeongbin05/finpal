<!-- <template>
    <div>
    <canvas id="canvas" ></canvas>

    </div>
  </template>
  
  <script setup>
  import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
  import * as THREE from 'three';
  
  
let scene = new THREE.Scene();
let camera = new THREE.PerspectiveCamera(30, 1);
camera.position.set(3, 1, 50);

let renderer = new THREE.WebGLRenderer({
    canvas: document.querySelector('#canvas'),
});

let ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(ambientLight);

let directionalLight = new THREE.DirectionalLight(0xffffff, 10);
directionalLight.position.set(1, 1, 1);
scene.background = new THREE.Color('white');
scene.add(directionalLight);

let loader = new GLTFLoader();

loader.load('front\vue-project\src\components\earth\scene.gltf', function (gltf) {
    scene.add(gltf.scene);

    function animate() {
    requestAnimationFrame(animate);
    gltf.scene.rotation.y += 0.01;
    renderer.render(scene, camera);
    }

    animate();
});

    
  
  </script>
  
  <style scoped>
  #canvas {
    width : 100px;
    height : 100px;
  }
  </style>
  -->
  <template>
    <div>
      <canvas id="canvas" width="100" height="100"  ></canvas>
    </div>
  </template>
  
  <script>
  import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
  import * as THREE from 'three';
  
  export default {
    mounted() {
      this.initThree();
    },
    methods: {
      initThree() {
        let scene = new THREE.Scene();
        scene.background = new THREE.Color('#2E155A');
        let camera = new THREE.PerspectiveCamera(30, 1);
        camera.position.set(3, 1, 50);
  
        let renderer = new THREE.WebGLRenderer({
          canvas: document.querySelector('#canvas'),
          antialias: true,
        });
        
        let ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
        scene.add(ambientLight);
  
        let directionalLight = new THREE.DirectionalLight(0xffffff, 10);
        directionalLight.position.set(1, 1, 1);
        scene.add(directionalLight);
  
        let loader = new GLTFLoader();
  
        loader.load('/earth/scene.gltf', function (gltf) {
          scene.add(gltf.scene);
  
          function animate() {
            requestAnimationFrame(animate);
            gltf.scene.rotation.y += 0.01;
            renderer.render(scene, camera);
          }
  
          animate();
        });
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add any additional styles here if needed */

  </style>
  