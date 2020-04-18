import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CompaniesComponent } from './companies/companies.component';
import { VacanciesComponent } from './vacancies/vacancies.component';
import { CompanyDetailComponent } from './company-detail/company-detail.component';


const routes: Routes = [
  { path: '', redirectTo: 'companies', pathMatch: 'full'},
  { path: 'companies', component: CompaniesComponent},
  { path: 'vacancies', component: VacanciesComponent},
  { path: 'companies/:id/vacancies', component: VacanciesComponent},
  { path: 'companies/:id', component: CompanyDetailComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
