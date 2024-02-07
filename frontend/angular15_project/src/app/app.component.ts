import { Component,OnInit } from '@angular/core';
import { SharedService } from './shared.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'angular15_project';
  site_logo: string='';
  constructor(private sharedService: SharedService) {}

  ngOnInit() {}
  //   this.sharedService.getLogoPath().subscribe(
  //     (logoPath: string) => {
  //       this.site_logo = logoPath;
  //     },
     
  // )};
}
