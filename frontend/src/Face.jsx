import { FaceMesh } from "@mediapipe/face_mesh";
import {
  FACEMESH_RIGHT_EYE,
  FACEMESH_RIGHT_EYEBROW,
  FACEMESH_RIGHT_IRIS,
  FACEMESH_LEFT_EYE,
  FACEMESH_LEFT_EYEBROW,
  FACEMESH_LEFT_IRIS,
  FACEMESH_FACE_OVAL,
  FACEMESH_LIPS,
  FACEMESH_TESSELATION,
} from "@mediapipe/face_mesh";
import React, { useRef, useEffect, useState } from "react";
import * as cam from "@mediapipe/camera_utils";
import { drawConnectors } from "@mediapipe/drawing_utils";
import Webcam from "react-webcam";
import './App.css';
import "./components/style.css";

import Button from 'react-bootstrap/Button';

import { ToggleSwitch } from 'flowbite-react';
import axios from 'axios';
import Toggle from "./components/Toggle";

function Face() {

  const videoRef = useRef(null);
  const webcamRef = useRef(null);
  const cameraRef = useRef(null);
  const canvasRef = useRef(null);
  const faceMeshRef = useRef(null);
  const [aiEnabled, setAiEnabled] = useState(false);
  const [draww, setDraww] = useState(false);
  var person_exists = false;
  const [check, setCheck] = useState("disabled");

  const handleStart = () => {
    setAiEnabled((aiEnabled) => !aiEnabled)
  }

  const changeDraw = () => {
    setDraww((draww) => !draww);
  }


  const [imageSent, setImageSent] = useState(false);
  const captureImage = async () => {
    // Создаем снимок экрана
    
    const videoElement = webcamRef.current.video;
    const canvasElement = canvasRef.current;
    canvasElement.width = videoElement.videoWidth;
    canvasElement.height = videoElement.videoHeight;
    const ctx = canvasElement.getContext('2d');
    ctx.drawImage(videoElement, 0, 0, videoElement.videoWidth, videoElement.videoHeight);
  
    // Получаем данные с Canvas в формате base64
    const imageData = canvasElement.toDataURL('image/jpeg');
    
    axios.post('https://jsonplaceholder.typicode.com/posts', {image: imageData})
    .then(response => {
      const data= response
      console.log(data)
    })
    .catch(error => {
        console.error('Error:', error);
    });

  };


  function checking(person_detected) {
    person_detected 
    ? setCheck("✅")
    : setCheck("❌"); 
    
  }

useEffect(()=>{
    if (check=="✅")
    captureImage()
},[check])

  useEffect(() => {
    const onResults = (results) => {

      const videoWidth = webcamRef.current.video.videoWidth;
      const videoHeight = webcamRef.current.video.videoHeight;
      // Set canvas width
      canvasRef.current.width = videoWidth;
      canvasRef.current.height = videoHeight;

      const canvasElement = canvasRef.current;
      const canvasCtx = canvasElement.getContext("2d");
      canvasCtx.save();
      canvasCtx.clearRect(0, 0, canvasElement.width, canvasElement.height);
      canvasCtx.drawImage(
        results.image,
        0,
        0,
        canvasElement.width,
        canvasElement.height
      );

      if (results.multiFaceLandmarks && aiEnabled) {
        if (results.multiFaceLandmarks.length) {
          
          person_exists = true;
          if (draww) {
            for (const landmarks of results.multiFaceLandmarks) {
              drawConnectors(canvasCtx, landmarks, FACEMESH_TESSELATION, { color: '#C0C0C070', lineWidth: 1 });
              drawConnectors(canvasCtx, landmarks, FACEMESH_RIGHT_EYE, { color: '#ac30ff' });
              drawConnectors(canvasCtx, landmarks, FACEMESH_RIGHT_EYEBROW, { color: '#ac30ff' });
              drawConnectors(canvasCtx, landmarks, FACEMESH_RIGHT_IRIS, { color: '#ac30ff' });
              drawConnectors(canvasCtx, landmarks, FACEMESH_LEFT_EYE, { color: '#30b3ff' });
              drawConnectors(canvasCtx, landmarks, FACEMESH_LEFT_EYEBROW, { color: '#30b3ff' });
              drawConnectors(canvasCtx, landmarks, FACEMESH_LEFT_IRIS, { color: '#30b3ff' });
              drawConnectors(canvasCtx, landmarks, FACEMESH_FACE_OVAL, { color: '#E0E0E0' });
              drawConnectors(canvasCtx, landmarks, FACEMESH_LIPS, { color: '#E0E0E0' });
            }
          }
        //   console.log(draww)
          
        } else {
          
          person_exists = false;

         

        }
        checking(person_exists);


      }
      canvasCtx.restore();

    }

    if (aiEnabled) {
      if (faceMeshRef.current) {
        console.log(faceMeshRef.current)
        faceMeshRef.current.onResults(onResults)
      }
      else {
        const faceMesh = new FaceMesh({
          locateFile: (file) => {
            return `https://cdn.jsdelivr.net/npm/@mediapipe/face_mesh/${file}`;
          },
        });

        faceMesh.setOptions({
          maxNumFaces: 1,
          minDetectionConfidence: 0.5,
          minTrackingConfidence: 0.5,

        });

        faceMesh.onResults(onResults);

        faceMeshRef.current = faceMesh;
      }
      if (cameraRef.current) {
        cameraRef.current.h.onFrame = async () => {
          await faceMeshRef.current.send({ image: webcamRef.current.video });
        }
      } else {
        const camera = new cam.Camera(webcamRef.current.video, {
          onFrame: async () => {
            await faceMeshRef.current.send({ image: webcamRef.current.video });
          },
          width: 640,
          height: 480,
        });
        camera.start();
        cameraRef.current = camera;
      }
    } else {
      console.log("turning off")

      if (cameraRef.current) {
        cameraRef.current.h.onFrame = () => {
          const videoWidth = webcamRef.current.video.videoWidth;
          const videoHeight = webcamRef.current.video.videoHeight;

          // Set canvas width
          canvasRef.current.width = videoWidth;
          canvasRef.current.height = videoHeight;

          const canvasElement = canvasRef.current;
          const canvasCtx = canvasElement.getContext("2d");
          canvasCtx.save();
          canvasCtx.clearRect(0, 0, canvasElement.width, canvasElement.height);
          canvasCtx.drawImage(
            webcamRef.current.video,
            0,
            0,
            canvasElement.width,
            canvasElement.height
          );
        };
        
        setCheck("disabled")
      }
    }


  }, [aiEnabled, draww]);

  useEffect(() => {

  }, [])

  return ( 
    <div className="w-[960px] m-auto mt-10"> 
    
    
      
 
      <div className="mirror flex"> 
        <Webcam 
          ref={webcamRef} 
          className="fixed inset-x-0  rounded-lg m-auto w-[960px] "
          
        /> 
        <canvas 
          ref={canvasRef} 
          className="output_canvas m-auto relative rounded-lg w-[960px] h-[720px] " 
        /> 
      </div> 
 
      <div
        className="flex mx-auto  pt-5"
       > 
        <Button variant="light" className="w-[300px] bg-gray-950 text-4xl" onClick={handleStart}>
          {check=="✅"
            ?'Stop'
            :'Start'
          }
        </Button> 
        <div  className="flex m-auto max-w-max items-center" > 
         
              <a>{check}</a> 
           
        </div> <div className="flex w-[320px] h-[100px] text-4xl items-center" > 
        {aiEnabled&&
        <>
        Маска &nbsp;
        <Toggle toggled={draww} onClick={changeDraw} /> 
        </>
        
     
        }
         </div> 
      </div>
        {/* <LoginForm></LoginForm> */}
        
        
    </div > 
  ); 
} 
 
export default Face;