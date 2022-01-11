import React, {useEffect, useState} from "react";
import {Button,Card, CardMedia, Grid, makeStyles} from "@material-ui/core";
import axios from "axios";
import { CardActions} from "@mui/material";
import {Link} from "react-router-dom";


const useStyles = makeStyles(() => ({
    container: {
        display: "flex",
        flexDirection: "row",
        justifyContent: "center",
        alignItems: "baseline",
        marginTop: 20,
        padding: 30
    },
    card: {
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "baseline"
    }
}))

export const ResultImg = ({data}) => {
    const domen = "https://skbgen.herokuapp.com";
/*    const domen = "http://127.0.0.1:8000"*/

    const styles = useStyles();
    const [post, setPosts] = useState([]);


    useEffect(() => {
        const selectedCategory = data.categorySelector;
        const text_fields = [data.postTitle, data.postText];
        const dataReformed = new FormData();
        dataReformed.append("image", (selectedCategory === 'checks' || selectedCategory === 'triangle_mask')
            ? data.files[0] : '');
        dataReformed.append("gen_type", selectedCategory);
        dataReformed.append("params", `color=${data.colorSelector}`);
        dataReformed.append("text_fields", (selectedCategory === 'checks' || selectedCategory === 'triangle_mask' || selectedCategory === 'typography')
            ? text_fields[0]
            : text_fields.join(";"));

        const config = {
            headers: {
                'content-type': 'multipart / form-data'
            }
        }

        const getImageByID = async () => {
            console.log(dataReformed);
            const response = await axios.post(`${domen}/api/v1/generator/new/`,
                dataReformed,
                config);
            setPosts(response.data);
        }

        getImageByID();
    }, [])

    const imgLink = `${domen}/api/v1/generator/get/?id=${post.id}`;

    console.log(post);
    return (
        <>
            <Grid container className={styles.container}>
                {
                    <Grid item>
                        <Card>
                            <CardMedia
                                component="img"
                                alt="result"
                                height="400"
                                width='400'
                                image={imgLink}
                            />

                            <CardActions className={styles.card}>
                                <Button component={Link} download target="_blank" to={`/api/v1/generator/get/?id=${post.id}`} size="large" variant="outlined">
                                    Скачать
                                </Button>
                            </CardActions>
                        </Card>
                    </Grid>
                }
            </Grid>
        </>
    );
}