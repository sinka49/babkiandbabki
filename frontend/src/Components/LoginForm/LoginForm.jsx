import s from "./LoginForm.module.css";
import { TextField } from "@mui/material";
import { Link } from "react-router-dom";

const LoginForm = ({ setIsAuthorized }) => {
  return (
    <div className={s.loginForm}>
      <div className={s.header}>
        <div className={s.number}>Номер телефона</div>
        <Link to="/">
          <button className={s.leftBtn} onClick={() => {}}>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="22"
              height="22"
              viewBox="0 0 22 22"
              fill="none"
            >
              <path
                d="M8.14214 13.799L13.799 8.14215M13.799 13.799L8.14214 8.14215M18.0416 18.0416C21.9307 14.1526 21.9307 7.7886 18.0416 3.89951C14.1525 0.0104261 7.78859 0.0104261 3.8995 3.89951C0.0104106 7.7886 0.0104106 14.1526 3.8995 18.0416C7.78859 21.9307 14.1525 21.9307 18.0416 18.0416Z"
                stroke="#ADADAD"
                strokeWidth="1.5"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
            </svg>
          </button>
        </Link>
      </div>

      <TextField
        fullWidth
        id="fullWidth"
        autoFocus={true}
        defaultValue="+7"
        placeholder={""}
        type="tel"
      />

      <div className={s.footer}>
        <Link to="#">Обработка личных данных</Link>
        <Link to="/">
          <button className={s.footerBtn} onClick={() => setIsAuthorized(true)}>
            Зарегистрироваться
          </button>
        </Link>
      </div>
    </div>
  );
};

export default LoginForm;
