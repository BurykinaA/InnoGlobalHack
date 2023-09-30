import { useEffect, useState } from 'react'
import React from 'react';
import './App.css'
import Face from './Face';
import { FileInput, Checkbox, Label } from 'flowbite-react';
import axios from 'axios';




function App() {
  const [check, setCheck] = useState(false)

  const handlePost =  (event) => {
    const selectedFile = event.target.files[0];

    if (selectedFile) {
      const reader = new FileReader();

      reader.onload = async (e) => {
       
          const base64Image = e.target.result;

          // Выполните POST-запрос на сервер, отправив изображение в формате base64
          axios.post('https://jsonplaceholder.typicode.com/posts', {
            image: base64Image,
          })
          .then(response => {
            const data= response
            console.log(data)
          })
          .catch(error => {
              console.error('Error:', error);
          });
        
      };

      reader.readAsDataURL(selectedFile);
    }
  };
 
  return (
    
    <div className='w-[96%]  mx-auto p-2 '>
      <div className="flex items-center my-3 gap-2">
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
        
      </div>
      
      {check&& <Face/>}
  </div>
  )
}

export default App
