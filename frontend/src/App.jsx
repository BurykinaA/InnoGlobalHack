import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import axios from 'axios';
import Face from './Face'


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
    <div >
      
       <div className='nav'>
       <div class="checkbox-rect">
        <input type="checkbox" id="checkbox-rect1" name="check" onChange={(e)=>setCheck(e.target.checked)}/>
        <label for="checkbox-rect1">Распознавание с камеры</label>
      </div>
      <input id="file" type="file" onChange={handlePost} /> 
      </div>
      
      
   
     

        {check&& <Face/>}
     
    </div>
  )
}

export default App
