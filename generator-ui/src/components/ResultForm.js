import React from "react";
import {ResultImg} from "./ResultImage";
import {MainContainer} from "../conteiners/MainContainer";
import {Link} from "react-router-dom";
import {useData} from "./DataContext";
import {Button} from "@mui/material";

export const ResultForm = () => {
    const { data } = useData();
    return (
        <MainContainer>
            <ResultImg data={data}/>

            <Button component={Link} to="/" variant="outlined" color="error" size="small">
                Назад
            </Button>
        </MainContainer>
    );
}