const webpack = require('webpack');
const merge = require('webpack-merge');
const common = require('./webpack.common.js');

module.exports = merge(common, {
  mode: 'production',
  plugins : [
    new webpack.DefinePlugin({
        SERVICE_URL: JSON.stringify("http://192.168.0.190/api")
      })
  ]
});