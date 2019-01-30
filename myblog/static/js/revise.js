const revisePadding = () => {
  const headerHeight = document.getElementsByTagName("header")[0].clientHeight;
  const footerHeight = document.getElementsByTagName("footer")[0].clientHeight;
  const overlay = document.getElementById("common_overlay");
  overlay.style.paddingTop = headerHeight + "px";
  overlay.style.paddingBottom = footerHeight + "px";
};

window.onload = revisePadding;
window.onresize = revisePadding;
