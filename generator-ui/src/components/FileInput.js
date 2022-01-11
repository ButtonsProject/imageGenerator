import React from "react";
import Dropzone from "react-dropzone";
import {Controller} from "react-hook-form";
import {makeStyles} from "@material-ui/core/styles";
import Paper from "@material-ui/core/Paper";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemIcon from "@material-ui/core/ListItemIcon";
import ListItemText from "@material-ui/core/ListItemText";
import InsertDriveFile from "@material-ui/icons/InsertDriveFile";
import {Button} from "@mui/material";
import {Delete} from "@material-ui/icons";

const useStyles = makeStyles(() => ({
    root: {
        fontFamily: "Roboto",
        padding: "10px",
        marginTop: "10px",
        color: "#666666"
    },
    icon: {
        marginTop: "10px",
        fontSize: "36px",
    },
}));

export const FileInput = ({ control, name }) => {
    const styles = useStyles();

    return (
        <Controller
            control={control}
            name={name}
            defaultValue={[]}
            render={({field: {onChange, onBlur, value} }) => (
                <>
                    <Dropzone onDrop={onChange} accept={'image/jpeg, image/png'} maxFiles={1}>
                        {({ getRootProps, getInputProps }) => (
                            <Paper
                                variant="outlined"
                                className={styles.root}
                                {...getRootProps()}
                            >
                                <input {...getInputProps()} name={name} onBlur={onBlur} type='file'/>
                                <p>Вставьте или перетащите картинку</p>
                            </Paper>
                        )}
                    </Dropzone>
                    <List>
                        {value?.map((f, index) => (
                            <ListItem key={index}>
                                <ListItemIcon>
                                    <InsertDriveFile />
                                </ListItemIcon>
                                <ListItemText primary={f.name} secondary={f.size} />
                                <Button variant="fab" aria-label="delete" onClick={() => {
                                    value?.splice(index, 1);
                                    onBlur();
                                } }> <Delete/> </Button>
                            </ListItem>
                        ))}
                    </List>
                </>
            )}
        />
    );
};