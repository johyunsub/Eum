//이미지파일들 한번에 import 시키기 위한 js파일
const files = require.context('.', false, /\.png$/)
const modules = {}
files.keys().forEach((key) => {
     if (key === './index.js') return
     modules[key.replace(/(\.\/|\.png)/g, '')] = files(key)
})
export default modules