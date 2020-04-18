import { Component, OnInit } from '@angular/core';
import { LoginService } from '../login.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(
    private loginService: LoginService
  ) { }

  ngOnInit(): void {
  }

  login(username: string, password: string) {
    this.loginService.login(username, password).subscribe(
      response => {
        localStorage.setItem("token", response.token)
      });
  }

  logout() {
    localStorage.removeItem("token");
  }

}
