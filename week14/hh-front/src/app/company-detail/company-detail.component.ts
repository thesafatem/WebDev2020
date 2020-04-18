import { Component, OnInit } from '@angular/core';
import { Company, Vacancy } from '../models';
import { CompanyService } from '../company.service';
import { VacancyService } from '../vacancy.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-company-detail',
  templateUrl: './company-detail.component.html',
  styleUrls: ['./company-detail.component.css']
})
export class CompanyDetailComponent implements OnInit {

  company: Company;
  vacancies: Vacancy[];

  constructor(
    private route: ActivatedRoute,
    private companyService: CompanyService,
    private vacancyService: VacancyService
  ) { }

  ngOnInit(): void {
    this.getCompany();
  }

  getCompany() {
    this.route.params.subscribe(params => {
      const id = +params['id'];
      this.companyService.getCompany(id).subscribe(company => {
        this.company = company
      });
      this.vacancyService.getVacancyListByCompany(id).subscribe(vacancies => {
        this.vacancies = vacancies
      });
    });
  }

}
