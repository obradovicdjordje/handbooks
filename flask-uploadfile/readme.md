# Primer za angular file upload funkcionalnost 

## 1
https://github.com/leon/angular-upload

1. dodati u index.html <script src="js/angular-upload.min.js" type="text/javascript" ></script>
2. dodati u /www/app/js/app.js 
        angular.module('app', ['lr.upload']);
3. ubaciti u login deo 
    <div
      class="btn btn-primary btn-upload"
      upload-button
      url="/upload"
      on-success="onSuccess(response)"
    >Upload</div>


## 2 https://github.com/nervgh/angular-file-upload
1. kopirati 
    /home/djordje/Downloads/angular-file-upload.min.js.map
    /home/djordje/Downloads/angular-file-upload.min.js
2. dodati u index.html
   
