console.log('hello from app.js ... or so')

const getElement = (selector) => {
  const element = document.querySelector(selector)

  if (element) return element
  throw Error(
    `Please double check your class names, there is no ${selector} class`
  )
}

const links = getElement('.nav-links')
const navBtnDOM = getElement('.nav-btn')

navBtnDOM.addEventListener('click', () => {
  links.classList.toggle('show-links')
})

const date = getElement('#date')
const currentYear = new Date().getFullYear()
date.textContent = currentYear

// Auto-hide flash messages after 4 seconds
setTimeout(() => {
  document.querySelectorAll(".flash-message").forEach(msg => {
    msg.style.opacity = "0";
    setTimeout(() => msg.remove(), 500);
  });
}, 4000);
