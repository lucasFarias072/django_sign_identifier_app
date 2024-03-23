

document.body.style.border = '#222 solid 1px'

function rgb() {
  const inks = [...Array(256).keys()]

  let red = Math.floor(Math.random() * inks.length)
  let green = Math.floor(Math.random() * inks.length)
  let blue = Math.floor(Math.random() * inks.length)

  return `rgba(${inks[red]},${inks[green]},${inks[blue]})`
}

function addNewResourcesToMainForm() {
    // Dando um atrib. "id" para a tag d formulário
    formEl.setAttribute('id', 'algorithm-form')

    // Pegando o primeiro input do formulário e add recursos que não sei fazer pelo Django
    formOnlyInput.setAttribute('placeholder', 'Digite seu aniversário no formato (dd/mm/yyyy)')
    formOnlyInput.setAttribute('size', '50')
}

function blinkingBoxShadow({delay}) {
  let seconds = new Date().getSeconds()
  let secondIsDivisibleBy5 = seconds % delay === 0
  if (secondIsDivisibleBy5) {
    // Mudando a sombra atrás das duas seções
    firstSectionEl.style.boxShadow = `0 0 10px ${rgb()}`
    secondSectionEl.style.boxShadow = `0 0 10px ${rgb()}`
  }
}

function appendSignImage({djangoContextVar, signsLabelsTag, imgTag, signsArray}) {

  if (djangoContextVar.textContent != '') {
    signsLabelsTag.forEach(function(signName, i) {
      // If the text processed on the backend is the in between one the texts inside "signs" below
      if (djangoContextVar.textContent.trim() === signName) {
        // The image shown will the corresponding to the path set in signsImgPaths
        imgTag.setAttribute('src', `${signsArray[i]}`)
      }
    })
  }
}

const signs = [
  'Capricórnio', 'Aquário', 'Peixes', 'Aries', 'Touro', 'Gêmeos',
  'Câncer', 'Leão', 'Virgem', 'Libra', 'Escorpião', 'Sagitário'
]

/*
I tried all I could to implement images using Django syntax, and I could not succeed
Importing css and javascript with "{% static '' %}" syntax seems alright, but not into "src" value on image tags
I tried something like this: "{% static 'img/signs/capricorn.gif' %}" dynamically inserted, and the image did not load
Errors on the html console were shown (right button on template and "inspect" option)
*/
const returnTwoLevels = "../../"
const steadyPath = "static/img/signs/"
const signsImgPaths = [
    `${returnTwoLevels}${steadyPath}capricorn.gif`,
    `${returnTwoLevels}${steadyPath}aquarius.gif`,
    `${returnTwoLevels}${steadyPath}pisces.gif`,
    `${returnTwoLevels}${steadyPath}aries.gif`,
    `${returnTwoLevels}${steadyPath}taurus.gif`,
    `${returnTwoLevels}${steadyPath}gemini.gif`,
    `${returnTwoLevels}${steadyPath}cancer.gif`,
    `${returnTwoLevels}${steadyPath}leo.gif`,
    `${returnTwoLevels}${steadyPath}virgo.gif`,
    `${returnTwoLevels}${steadyPath}libra.gif`,
    `${returnTwoLevels}${steadyPath}scorpio.gif`,
    `${returnTwoLevels}${steadyPath}sagittarius.gif`
]

// Elementos
const formEl = document.querySelector('form')
const formOnlyInput = document.getElementById('id_birthday')
const firstSectionEl = document.querySelector('.mother-el-section-1st')
const secondSectionEl = document.querySelector('.mother-el-section-2nd')
const signEl = document.getElementById('sign')
const signImgEl = document.getElementById('sign-img')

// Dar um "id" ou formulário, add informação instrutiva ou input e aumentar sua largura
addNewResourcesToMainForm()

const signAlgorithmLoop = setInterval(() => {
  // Miscelânia
  blinkingBoxShadow({delay: 5})

  // Trocar a imagem de acordo com o texto enviado p/ a tag <td id="sign"> em "index.html"
  appendSignImage({djangoContextVar: signEl, signsLabelsTag: signs, imgTag: signImgEl, signsArray: signsImgPaths})
})
