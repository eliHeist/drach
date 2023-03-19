//#region global variables
const send_mail_url = document.querySelector('#mailurl').textContent
//#endregion

// get csrf token
let csrf = () => {
   token = document.getElementById('token').firstElementChild.value;
   return token;
};
//#endregion

//#region UI
class UI {
   static showAlert = (message, className) => {
      const div = document.createElement('div');
      div.className = `rounded-pill alert alert-${className}`;
      div.id = 'popup-alert';
      div.appendChild(document.createTextNode(message));
      const body = document.querySelector('#banner');
      body.insertBefore(div, body.firstElementChild);
      trackAlertWidth();
      alert = document.querySelector('#popup-alert');

      setTimeout(() => alert.classList.add('animate'), 200);
      setTimeout(() => alert.classList.remove('animate'), 3000);
      setTimeout(() => alert.remove(), 4000);
   }
}
const trackAlertWidth = () => {
   alert = document.getElementById('popup-alert');
   dev_width = document.getElementById('banner').clientWidth;
   alert_left = (dev_width - alert.clientWidth) / 2;
   alert.style.left = `${alert_left}px`;
}
//#endregion

//#region Objects
class Subscriber{
   constructor(email) {
      this.email = email;
   }
}

class Mail{
   constructor(date, email, phone, name, session, eventName, moreInfo) {
      this.date = date;
      this.email = email;
      this.phone = phone;
      this.name = name;
      this.session = session;
      this.eventName = eventName;
      this.moreInfo = moreInfo;
   }
}
//#endregion

//#region api functions
class Api{
   // static addSubscriber = async (subscriber) => {
   //    const response = await fetch(`${api_url}subscribers/`, {
   //       method: 'POST',
   //       headers: {
   //          Accept: 'application/json',
   //          'Content-Type': 'application/json',
   //          'X-CSRFToken': csrf(),
   //       },
   //       body: JSON.stringify(subscriber),
   //    });
   //    const data = await response.json();
   //    if (data === 'success') {
   //       UI.showAlert('😉 You Joined Our Newsletter', 'success');
   //    }
   //    else {
   //       UI.showAlert('😒 Failure', 'danger');
   //    }
   // }

   static sendMail = async (mail) => {
      const response = await fetch(send_mail_url, {
         method: 'POST',
         headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf(),
         },
         body: JSON.stringify(mail),
      });
      
      console.log(response.body);
      const data = await response.json();
      if (data === 'SUCCESS') {
         // clear fields
         clearFields()
         UI.showAlert('✔️ Sent successfully', 'success');
      }
      else if(!response.ok){
         UI.showAlert('❌ Failed try again later', 'danger');
      }
      else {
         UI.showAlert('❌ Sorry, failed to reach server', 'danger');
      }
   }
}
//#endregion

//#region form on homepage
// if (document.URL === root_url) {
//    document.getElementById('newsletter_form').addEventListener('submit', (e) => {
//       // prevent submit
//       e.preventDefault();
   
//       // get email
//       const email = document.getElementById('id_email');
      
//       const subscriber = new Subscriber(email.value);
//       Api.addSubscriber(subscriber);
   
//       email.value = '';
//    });
// }
//#endregion


//#region send mail form
   // get subject, email, text, name
   const name = document.getElementById('name')
   const phone = document.getElementById('phone')
   const email = document.getElementById('email')
   const session = document.getElementById('session');
   const date = document.getElementById('date');
   const eventName = document.getElementById('eventName');
   const moreInfo = document.getElementById('moreInfo');
   document.getElementById('send-mail-form').addEventListener('submit', (e) => {
      // prevent submit
      e.preventDefault();
      // instantiate mail
      const mail = new Mail(date.value, email.value, phone.value, name.value, session.value, eventName.value, moreInfo.value);

      // send to backend
      Api.sendMail(mail);
   
      
   });

// clear fields
const clearFields = () => {
   fname.value = ''
   lname.value = ''
   subject.value = ''
   msg.value = ''
   email.value = ''
}
//#endregion

