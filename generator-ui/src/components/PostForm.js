import React from "react";
import {Form} from "./Form";
import {Input} from "./Input";
import {useForm} from "react-hook-form";
import {MainContainer} from "../conteiners/MainContainer";
import {PrimaryButton} from "./PrimaryButton";
import {useHistory} from "react-router-dom";
import {FileInput} from "./FileInput";
import {useData} from "./DataContext";
import {ColorSelector, NewCategorySelector} from "./CategorySelector";
import * as yup from "yup";
import {yupResolver} from "@hookform/resolvers/yup";


export const PostForm = () => {
    const history = useHistory();
    const {data, setValues} = useData();
    const schema = yup.object().shape({
        categorySelector: yup.string(),
        postTitle: yup
            .string()
            .required("Заголовок поста обязателен"),
        postText: yup
            .string()
            .when("categorySelector",
                {
                    is: "high_article",
                    then: yup.string().required("Текст поста обязателен")
                }),
        files: yup
            .array()
            .when("categorySelector",
                {
                    is: "checks",
                    then: yup.array().min(1)
                })
            .when("categorySelector",
                {
                    is: "triangle_mask",
                    then: yup.array().min(1)
                }),
    });
    const {register, control, handleSubmit, watch, formState: {errors}} = useForm({
        defaultValues: {
            postTitle: data.postTitle,
            postText: data.postText,
            categorySelector: data.categorySelector,
            colorSelector: data.colorSelector,
            files: data.files
        },
        mode: "onBlur",
        resolver: yupResolver(schema)
    });


    const selectedCategory = watch("categorySelector");

    const onSubmit = (data) => {
        console.log(selectedCategory);
        console.log(data);
        setValues(data);
        history.push('/result');

    };

    return <MainContainer>
        <Form onSubmit={handleSubmit(onSubmit)}>
            <NewCategorySelector name="categorySelector" control={control}/>

            {
                (selectedCategory === "checks" || selectedCategory === "triangle_mask") && (
                    <>
                        <Input
                            {...register("postTitle")}
                            id="postTitle"
                            type="text"
                            label="Введите заголовок поста"
                            name="postTitle"
                            error={!!errors.postTitle}
                            helperText={errors?.postTitle?.message}
                        />

                        {(selectedCategory === "triangle_mask") && (<ColorSelector control={control}/>)}

                        <FileInput name="files" control={control}/>
                    </>
                )
            }

            {
                selectedCategory === 'high_article' && (
                    <>
                        <Input
                            {...register("postTitle")}
                            id="postTitle"
                            type="text"
                            label="Введите заголовок поста"
                            name="postTitle"
                            error={!!errors.postTitle}
                            helperText={errors?.postTitle?.message}
                        />

                        <Input
                            {...register("postText")}
                            id="postText"
                            type="text"
                            label="Введите текст поста"
                            name="postText"
                            error={!!errors.postText}
                            helperText={errors?.postText?.message}
                        />

                        <ColorSelector control={control}/>

                    </>
                )
            }

            {
                selectedCategory === 'typography' && (
                    <>
                        <Input
                            {...register("postTitle")}
                            id="postTitle"
                            type="text"
                            label="Введите заголовок поста"
                            name="postTitle"
                            error={!!errors.postTitle}
                            helperText={errors?.postTitle?.message}
                        />

                        <ColorSelector control={control}/>

                    </>
                )
            }

            <PrimaryButton>Отправить</PrimaryButton>
        </Form>
    </MainContainer>
}