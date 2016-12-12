function handleCodeUploadBtn(event) {
  //Send the code to the server
  $.ajax({
    url: 'http://127.0.0.1:1337/code/string',
    type: 'POST',
    dataType: 'json',
    contentType: 'application/json',
    data: JSON.stringify({code : $('[name = "code"]').val()}),
    success: (data) => $('.stepBtn').prop('disabled', false) //Enable the step button
  });
}

function handleFileUploadBtn(event) {
  //Send the file to the server
  var file = $('[name = "file"]')[0].files[0];
  var formData = new FormData();
  formData.append('file', file);
  var xhr = new XMLHttpRequest();
  xhr.open('POST', 'http://127.0.0.1:1337/code/file', true);
  xhr.upload.onload = () => console.log('Upload complete');
  xhr.send(formData);
}

// function handleFileUploadBtn(event) {
//   //Send the file to the server
//   $.ajax({
//     url: 'http://127.0.0.1:1337/code/file',
//     type: 'POST',
//     dataType: 'json',
//     contentType: 'application/json',
//     data: JSON.stringify({code : $('[name = "file"]').val()}),
//     success: () => $('.stepBtn').prop('disabled', false) //Enable the step button
//   });
// }

function handleStepBtn(event) {
  //Get the step from the server
  $.get('http://127.0.0.1:1337/step', null, (data, status) => {
    var newVal = $('[name = "trace"]').val() + '\n' + String(data);
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

