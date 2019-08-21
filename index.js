const fetch = require('node-fetch');
const pitchfork = require('pitchfork');
const axios = require('axios');
const cheerio = require('cheerio');

axios.get()

const fetchListeners = () => {
    axios.get(`https://last.fm/music/Cat+Power/Moon+Pix/`).then(response => {
        const $ = cheerio.load(response.data);

        const listenEles = $('[class=js-date]')
        const timeEles = $('[class=js-value]')

        let timestamps = {};

        for (let i = 0; i < 100; i++){
            const listener = Object.values(listenEles[i])[3]
            const timestamp = Object.values(timeEles[i])[3]
            timestamps[listener.datetime] = timestamp['data-value'];
        }

        console.log(timestamps)

    })
    
};

const fetchDates = () => {
    axios.get(`https://last.fm/music/Cat+Power/Moon+Pix/`).then(response => {
        const $ = cheerio.load(response.data);

        const eles = $('time')
        console.log(eles)

        for (let i = 0; i < 750; i++){
            const attribs = Object.values(eles[i].attribs)
            if (attribs.length > 0 && attribs.typeof === 'string') console.log(attribs[1])
        }
    })
}
  
// review__

let key = '97f2454b452da1dd2984e44d65593737'



// fetchAlbum('Moon Pix', 'Cat Power')

fetchListeners();