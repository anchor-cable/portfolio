let headerHeight = 0;
let footerHeight = 0;
const overlay = document.getElementById("common_overlay");

const reviseMargin = () => {
  headerHeight = document.getElementsByTagName("header")[0].clientHeight;
  // footerHeight = document.getElementsByTagName("footer")[0].clientHeight;
  overlay.style.marginTop = headerHeight + "px";
  // overlay.style.marginBottom = footerHeight;
};

window.onload = reviseMargin();
window.onresize = reviseMargin();
