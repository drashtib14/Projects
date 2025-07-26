import React from 'react';
import Logo from './images/Logo.png';
import img1 from './images/img1.png';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBars } from '@fortawesome/free-solid-svg-icons';
import { faArrowUp } from '@fortawesome/free-solid-svg-icons';
import { faMagnifyingGlass } from '@fortawesome/free-solid-svg-icons';

function WebApp() {
  return (
    <div>
        {/* header start */}
      <div className='header_div'>
        <header>
            <div><img src={Logo} height={40}></img></div>
                <nav>
                    <ul>
                        <li><a>Home</a></li>
                        <li><a>About</a></li>
                        <li><a>Services</a></li>
                        <li><a>Contact</a></li>
                    </ul>
                </nav>
                <div>
                  <input placeholder='Search..' className='header_inp'></input>
                  <a><FontAwesomeIcon icon={faMagnifyingGlass} className='faSearch'/></a>
                </div>
                <a><FontAwesomeIcon icon={faBars} /></a>
        </header>
      {/* header end */}

      {/* section (first content) start */}
        <section className='header_sec'>
            <aside className='header_content_top'>
                <h1>First I wanted to be a veterinarian</h1>
                <p>Lorem Ipsum available but the majority have suffered alteration in some form, by injected humour randomised words.</p>
                <div>
                    <button className='btn1'>Contact Us</button>
                    <button className='btn2'>Our Service</button>
                </div>
            </aside>
            <aside className='header_content_btm'>
                <img src={img1} height={450}></img>
            </aside>
        </section>
      </div>
        {/* section (first content) end */}

      
        {/* section (second content) start */}
      <section>
        <div className='content2'>
              <div class="container_top">
                  <h1>As a veterinarian and lover of animals.</h1>

                  <p>Lorem Ipsum available but the majoty suffered alteration in some form, by humour randomised words.</p>

                  <button>Our Service</button>
              </div>

              <div class="container_btm">
                  <div class="box_container">
                      <div class="box"></div>
                      <div class="image">
                          {/* <i class="fa fa-play-circle fa-lg" aria-hidden="true"></i> */}
                      </div>
                  </div>
              </div>
        </div>
      </section>
      {/* section (second content) end */}

      {/* section (third content) start */}
      <section className='sec_title'>
        <div className='title_heading'>
            <h1>Title Here</h1>
            <p> Lorem Ipsum available, but the majority have <br/> suffered alteration in some form.</p>
        </div>

        <div className='title_flex'>
            <div>
                <img src="img/img3.png"></img>
                <h3>Veterinarian</h3>
                <p> Lorem Ipsum available, but <br/> the majority have suffered <br/> alteration in some.</p>
            </div>

            <div>
                <img src="img/img4.png"></img>
                <h3>Vaccination Care</h3>
                <p> Lorem Ipsum available, but <br/> the majority have suffered <br/> alteration in some.</p>
            </div>

            <div>
                <img src="img/img5.png"></img>
                <h3>Dental Care</h3>
                <p> Lorem Ipsum available, but <br/> the majority have suffered <br/> alteration in some.</p>
            </div>
        </div>
      </section>
        {/* section (third content) end */}

    {/* section (four content) start */}
        <section>
          <div className='vete_flex'>
            <div class="box_container">
              <div class="box1"></div>
                <div class="image1">
                    {/* <i class="fa fa-play-circle fa-lg" aria-hidden="true"></i> */}
                </div>
            </div>
        
            <div className='container_top'>
              <h1>As a veterinarian and lover of animals</h1>
              <p>Lorem Ipsum available but the majoty suffered alteration in some form, by humour randomised words</p>
              <button>Our Service</button>
            </div>
          </div>
        </section>
        {/* section (four content) end */}


        {/* section (fifth content) start */}
      <section className='sec_title'>
        <div className='title_heading'>
            <h1>Title Here</h1>
            <p> Lorem Ipsum available, but the majority have <br/> suffered alteration in some form.</p>
        </div>

        <div className='title_flex'>
            <div>
                <img src="img/img7.png"></img>
                <h3><del>$50</del><span>$30</span></h3>
                <button className='btn3'>Buy Now</button>
            </div>

            <div>
                <img src="img/img8.png"></img>
                <h3><del>$40</del><span>$25</span></h3>
                <button className='btn3'>Buy Now</button>
            </div>

            <div>
                <img src="img/img9.png"></img>
                <h3><del>$45</del><span>$20</span></h3>
                <button className='btn3'>Buy Now</button>
            </div>
        </div>
      </section>
        {/* section (fifth content) end */}


      {/* section (sixth content) start */}
      <section className='doc_sec'>
        <div className='title_heading'>
            <h1>The vetcare team</h1>
            <p> Lorem Ipsum available, but the majority have <br/> suffered alteration in some form.</p>
        </div>

        <div className='title_flex'>
            <div>
                <img src="img/img10.png"></img>
                <h3>Jennifer Mullen</h3>
                <p>VETERINARY</p>
            </div>

            <div>
                <img src="img/img11.png"></img>
                <h3>Sheeren Collins</h3>
                <p>ADMINISTRATION</p>
            </div>

            <div>
                <img src="img/img12.png"></img>
                <h3>Jennifer Mullen</h3>
                <p>VETERINARY</p>
            </div>
        </div>
      </section>
        {/* section (sixth content) end */}

        {/* section (seven content) start */}
          <section>
            <div className='seven_sec'>
              <div className='image3 div_flex'>
                <div>
                  <img src="img/icon1.png" height="65px"></img>
                  <p>+34793</p>
                  <h4>Happy Clients</h4>
                </div>

                <div>
                  <img src="img/icon2.png" height="65px"></img>
                  <p>+45382</p>
                  <h4>Department</h4>
                </div>

                <div>
                  <img src="img/icon3.png" height="65px"></img>
                  <p>+54762</p>
                  <h4>Vaccinations</h4>
                </div>
              </div>
            </div>
          </section>
        {/* section (seven content) end */}


      {/* section (last content) start */}
      <section className='doc_sec'>
        <div className='title_heading'>
            <h1>Recent Posts</h1>
            <p> Lorem Ipsum available, but the majority have <br/> suffered alteration in some form.</p>
        </div>

        <div className='title_flex comp'>
            <div>
                <img src="img/img14.png"></img>
                <h3>As a veterinarian and <br/> lover of animals</h3>
                <p>FEBRUARY 09, 2020</p>
                <p>Lorem Ipsum available, but the<br/> majority have suffered alteration<br/> in some words which look.</p>
                <p>Read More+</p>
            </div>

            <div>
                <img src="img/img15.png"></img>
                <h3>As a veterinarian and <br/> lover of animals</h3>
                <p>FEBRUARY 10, 2020</p>
                <p>Lorem Ipsum available, but the<br/> majority have suffered alteration<br/> in some words which look.</p>
                <p>Read More+</p>
            </div>

            <div>
                <img src="img/img16.png"></img>
                <h3>As a veterinarian and <br/> lover of animals</h3>
                <p>FEBRUARY 11, 2020</p>
                <p>Lorem Ipsum available, but the<br/> majority have suffered alteration<br/> in some words which look.</p>
                <p>Read More+</p>
            </div>
        </div>
      </section>
        {/* section (last content) end */}

    {/* footer start */}
      <footer>
        <div className='foot'>
        <div>
        <h2>About</h2>
          <div>
            <ul>
              <li>History</li>
              <li>Our Team</li>
              <li>Brand Guidelines</li>
              <li>Terms & Conditions</li>
              <li>Privacy Policy</li>
              <li></li>
            </ul>
          </div>
        </div>
        
       <div>
       <h2>Services</h2>
          <div>
            <ul>
              <li>How to Order</li>
              <li>Our Product</li>
              <li>Order Status</li>
              <li>Promo</li>
              <li>Payment Method</li>
              <li></li>
            </ul>
          </div>
       </div>

          <div>
            <span>Title Here</span>
            <p> Lorem Ipsum available, but the majority </p>
            <input className='footer_inp' placeholder='search..'></input>
            <a><FontAwesomeIcon icon={faMagnifyingGlass} className='faSearch1'/></a>
          </div>
        </div>
      </footer>
    {/* footer end */}

    {/* Scroll up button */}
        <div class="scroll-up"><a href="#">
          <FontAwesomeIcon icon={faArrowUp} />
        </a></div>
    </div>
  )
}

export default WebApp;