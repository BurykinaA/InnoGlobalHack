import { useEffect, useState } from 'react'
import React from 'react';
import './App.css'
import Face from './Face';
import { FileInput, Checkbox, Label } from 'flowbite-react';
import axios from 'axios';
import { PictureContext } from './context/context';



const URL= 'http://127.0.0.1:5000'
function App() {
  const [check, setCheck] = useState(false)
  const [picture, setPicture] = useState('')
  useEffect(()=>{
    setPicture(localStorage.getItem('response'))
  },[])
  const URL= 'http://127.0.0.1:5000'

  const handlePost =  (event) => {
    const selectedFile = event.target.files[0];

    if (selectedFile) {
      const reader = new FileReader();

      reader.onload = async (e) => {
       
          const base64Image = e.target.result;

          // Выполните POST-запрос на сервер, отправив изображение в формате base64
          axios.post(URL+'/api/photo', {
            photo: base64Image,
          })
          .then(response => {
            const data= response.data
            localStorage.setItem('response', data.photo)
            setPicture(data.photo)
            // console.log(data.id)
          })
          .catch(error => {
              console.error('Error:', error);
          });
        
      };

      reader.readAsDataURL(selectedFile);
    }
  };
 
  return (
    <PictureContext.Provider value={{picture, setPicture}}>
<div className='w-[96%]  mx-auto p-2 '>
      <div className="flex items-center my-3 ">
      <FileInput
        className='w-full mr-5'
          id="file"
          onChange={handlePost}
        />
        <Checkbox
          id="accept"
          onChange={(e)=>setCheck(e.target.checked)}
        />
        <label
          className="flex min-w-max dark:text-white text-2xl"
          htmlFor="agree"
        >
            Использовать камеру
        
        </label>
        <p className='mx-2'> {picture}</p>
        {/* <img className='inline-block object-cover ml-3 rounded-lg h-[82px] w-[82px]' src={picture}/> */}
      </div>
      
      {check&& <Face/>}
  </div>
    </PictureContext.Provider>
    
  )
}

export default App
