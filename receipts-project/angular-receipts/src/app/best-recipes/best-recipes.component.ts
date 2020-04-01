import { Component, OnInit } from '@angular/core';
import { RECIPES } from '../mock-recipes'

@Component({
  selector: 'app-best-recipes',
  templateUrl: './best-recipes.component.html',
  styleUrls: ['./best-recipes.component.css']
})
export class BestRecipesComponent implements OnInit {

  recipes = RECIPES;

  constructor() { }

  ngOnInit(): void {
  }

}
