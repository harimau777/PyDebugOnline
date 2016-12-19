function handleCodeUploadBtn(event) {
  //Send the code to the server
  $.ajax({
    url: 'http://127.0.0.1:1337/code/string',
    type: 'POST',
    dataType: 'json',
    contentType: 'application/json',
    data: JSON.stringify({code : $('[name = "code"]').val()}),
    success: () => $('.stepBtn').prop('disabled', false) //Enable the step button
  });
}

function handleFileUploadBtn(event) {
  if ($('[name = "file"]')[0].files.length === 0) {
    console.log('No file selected');
  } else {  
    //Send the file to the server
    const file = $('[name = "file"]')[0].files[0];
    const formData = new FormData();
    formData.append('file', file);
    const xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://127.0.0.1:1337/code/file', true);
    xhr.upload.onload = () => console.log('Upload complete');
    xhr.send(formData);
  }
}

function handleStepBtn(event) {
  //Get the step from the server
  $.get('http://127.0.0.1:1337/step', null, (data, status) => {
    const newVal = $('[name = "trace"]').val() + '\n' + String(data);
    $('[name = "trace"]').val(newVal); //Append to the trace text box
  }, 'json');
}

$(document).ready(() => {
  //Click upload (String)
  $('.codeUploadBtn').click(handleCodeUploadBtn);

  //Click upload (File)
  $('.fileUploadBtn').click(handleFileUploadBtn);

  //Click step
  $('.stepBtn').click(handleStepBtn);
});
