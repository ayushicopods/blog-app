const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    hot: true,
    liveReload: true,
  },
  publicPath: process.env.NODE_ENV === "production" ? "/static/" : "/",
});
