import { Component, OnInit } from '@angular/core';
import { Vacancy } from '../models';
import { VacancyService } from '../vacancy.service';

@Component({
  selector: 'app-vacancies',
  templateUrl: './vacancies.component.html',
  styleUrls: ['./vacancies.component.css']
})
export class VacanciesComponent implements OnInit {

  vacancies: Vacancy[];

  constructor(private vacancyService: VacancyService) { }

  ngOnInit(): void {
    this.getVacancyList();
  }

  getVacancyList() {
    this.vacancyService.getVacancyList()
    .subscribe(vacancies => {
      this.vacancies = vacancies
    });
  }

}
