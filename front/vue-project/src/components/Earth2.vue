<template>
    <div>
      <canvas id="canvas" width="500" height="500"  ></canvas>
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
        scene.background = new THREE.Color('#031321');
        let camera = new THREE.PerspectiveCamera(30, 1);
        camera.position.set(0, 1, 50);
  
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
.canvas {
  display :flex;
  justify-content: center;
  align-items: center;
  padding :0 ;

}
  </style>
  