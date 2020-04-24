function initialFun(){
    //实现页面元素上下居中
    var mainDom = document.getElementById('page');
    var screenHeight = window.screen.height;
    var mainDomHeight = mainDom.offsetHeight;
    var iTop=(screenHeight-mainDomHeight)/3;
    console.log(mainDomHeight)
    mainDom.style.top = iTop + 'px';
}
window.onload = initialFun;