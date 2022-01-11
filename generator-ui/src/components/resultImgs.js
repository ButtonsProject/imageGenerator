import axios from "axios";
import React from "react";

export const imgs = () => {
    return ([
        {
            image: "http://127.0.0.1:8000/api/v1/generator/get/?id=28"
        }
    ])
}

const getResultImg = (data) => {
    console.log(data);
    const dataJSON = JSON.stringify({
        // "image": data.files,
        "gen_type": data.categorySelector.value,
        "params": "color=green",
        "text_fields": data.postTitle + ';' + data.postText
    })

    const config = {
        headers: {
            'Content-Type': 'application/json;charset=UTF-8'
        }
    }
    const getImageById = async () => axios.post('http://127.0.0.1:8000/api/v1/generator/new/',
        dataJSON,
        config)
        .then(res => {
            return 'http://127.0.0.1:8000/api/v1/generator/get/?id=' + res.data.id;
        })
        .catch(function (error) {
            console.log(error);
        });

    return getImageById();
}

export default getResultImg();