import React from "react";
import {makeStyles, Typography} from "@material-ui/core";

const useStyles = makeStyles((theme) =>({
    root: {
        margin: theme.spacing(5, 0, 2),
        textAlign: "center",
        fontSize: "72",
        color: "#00AA13"
    }
}))

export const Header = () => {
    const styles = useStyles()

    return <Typography className={styles.root} component='h1' variant='h3'>Генератор картинок</Typography>
}