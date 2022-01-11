import React from "react";
import Select from '@mui/material/Select';
import {makeStyles} from "@material-ui/core";
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import {Controller} from "react-hook-form";

const useStyles = makeStyles(() => ({
        root: {
            fontFamily: "Roboto",
            marginTop: "10px"
        }
    })
)

export const CategorySelector = ({control, name}) => {
    const styles = useStyles();

    return (
        <Controller
            name={name}
            control={control}
            render={({field}) => <Select
                className={styles.root}
                defaultValue={[]}
                {...field}
                options={[
                    {value: "checks", label: "Галочки"},
                    {value: "high_article", label: "Заголовок сверху без картинки"}
                ]}
            />}
        />
    );
};

export const NewCategorySelector = ({control}) => {

    return (
        <FormControl fullWidth margin='normal'>
            <InputLabel id='category-selector'>Выберите категорию поста</InputLabel>
            <Controller
                control={control}
                name='categorySelector'
                defaultValue={[]}
                render={({field: {name, onChange, value}}) => (
                    <Select
                        name={name}
                        id="categorySelector"
                        control={control}
                        labelId='category-selector'
                        label='Выберите категорию поста'
                        value={value}
                        onChange={onChange}
                    >
                        <MenuItem value={"checks"}>Галочки</MenuItem>
                        <MenuItem value={"high_article"}>Заголовок сверху без картинки</MenuItem>
                        <MenuItem value={"triangle_mask"}>Треугольная маска</MenuItem>
                        <MenuItem value={"typography"}>Типографика</MenuItem>
                    </Select>
                )}/>
        </FormControl>
    );
}

export const ColorSelector = ({control}) => {
    return (
        <FormControl fullWidth margin='normal'>
            <InputLabel id='color-selector'>Выберите основной цвет</InputLabel>
            <Controller
                control={control}
                name='colorSelector'
                defaultValue={["green"]}
                render={({field: {name, onChange, value}}) => (
                    <Select
                        name={name}
                        id="colorSelector"
                        control={control}
                        labelId='color-selector'
                        label='Выберите основной цвет'
                        value={value}
                        onChange={onChange}
                        required
                    >
                        <MenuItem value={"green"}>Зеленый</MenuItem>
                        <MenuItem value={"yellow"}>Желтый</MenuItem>
                        <MenuItem value={"orange"}>Оранжевый</MenuItem>
                    </Select>
                )}/>
        </FormControl>
    );
}

