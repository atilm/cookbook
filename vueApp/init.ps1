New-Item -Path . -Name ".bablerc.js" -ItemType "file"
New-Item -Path . -Name "webpack.config.js" -ItemType "file"
New-Item -Path . -Name "src" -ItemType "directory"

npm init
npm install vue vue-router vue-loader vue-template-compiler webpack webpack-cli webpack-dev-server babel-loader @babel/core @babel/preset-env css-loader vue-style-loader html-webpack-plugin rimraf -D
npm install bootstrap