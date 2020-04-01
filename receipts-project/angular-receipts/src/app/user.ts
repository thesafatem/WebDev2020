import { Recipe } from './recipe';

export interface User {
    id: number;
    login: string,
    password: string,
    name: string,
    last_name: string,
    email: string,
    saved_recipes: Recipe[],
    user_recipes: Recipe[]
}