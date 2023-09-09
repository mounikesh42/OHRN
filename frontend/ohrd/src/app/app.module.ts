import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { JobListComponent } from './job-list/job-list.component';
import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatListModule } from '@angular/material/list';
import { MatCardModule } from '@angular/material/card';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import { NavigationComponent } from './navigation/navigation.component';
import { LoginComponent } from './login/login.component';
import { RegistrationComponent } from './registration/registration.component';
import { RouterModule, Routes } from '@angular/router';
import { FormsModule } from '@angular/forms';
import {MatIconModule} from '@angular/material/icon';
import {MatMenuModule} from '@angular/material/menu';
import { PostJobComponent } from './post-job/post-job.component';
// import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { MatNativeDateModule, MatOptionModule } from '@angular/material/core';
import { MatSelectModule } from '@angular/material/select';
import {MatDatepickerModule} from '@angular/material/datepicker'; 
// MatNativeDateModule
const routes: Routes = [
  { path: '', component: JobListComponent },

  { path: 'login', component: LoginComponent },
  { path: 'registration', component: RegistrationComponent },
  { path: 'jobs', component: JobListComponent },
  { path: 'post', component: PostJobComponent },

  // Add other routes as needed
];
@NgModule({
  declarations: [
    AppComponent,
    JobListComponent,
    NavigationComponent,
    LoginComponent,
    RegistrationComponent,
    PostJobComponent
  ],
  imports: [
    MatNativeDateModule,
    BrowserModule,
    AppRoutingModule,
    MatDatepickerModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MatListModule,
    MatCardModule,
    MatInputModule,
    MatFormFieldModule,
    MatToolbarModule,
    MatButtonModule,
    FormsModule,
    MatIconModule,
    MatMenuModule,
    MatOptionModule,
    MatSelectModule,
    RouterModule.forRoot(routes)


  ],
  exports:[RouterModule],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
