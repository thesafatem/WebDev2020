import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from "@angular/common/http"
import { LoginResponse } from "./models"

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  BASE_URL = 'http://localhost:8000'
  constructor(private http: HttpClient) { }

  login(username, password): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(`${this.BASE_URL}/api/login/`, {
      username, password
    })
  }
}
