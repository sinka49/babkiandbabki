import s from "./Order.module.css";
import cn from "classnames";

const Order = ({ isOpen, setIsOrderOpen }) => {
  return (
    <div className={cn(s.wrapper, isOpen ? s.isOpen : "")}>
      <div>
        <div className={s.orderHeader}>
          <button className={s.leftBtn}>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
            >
              <path
                d="M13.3899 17.36L10.6399 14.61M13.3599 14.64L10.6099 17.39M8.80994 2L5.18994 5.63M15.1899 2L18.8099 5.63"
                stroke="#FF1C1C"
                strokeWidth="1.5"
                strokeMiterlimit="10"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
              <path
                d="M2 7.85C2 6 2.99 5.85 4.22 5.85H19.78C21.01 5.85 22 6 22 7.85C22 10 21.01 9.85 19.78 9.85H4.22C2.99 9.85 2 10 2 7.85Z"
                stroke="#FF1C1C"
                strokeWidth="1.5"
              />
              <path
                d="M3.5 10L4.91 18.64C5.23 20.58 6 22 8.86 22H14.89C18 22 18.46 20.64 18.82 18.76L20.5 10"
                stroke="#FF1C1C"
                strokeWidth="1.5"
                strokeLinecap="round"
              />
            </svg>
          </button>
          <span>Ваш заказ</span>
          <button className={s.leftBtn} onClick={() => setIsOrderOpen(false)}>
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
        </div>
        <div className={s.items}>
          <div className={s.card}>
            <div className={s.cardLeft}>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="68"
                height="68"
                viewBox="0 0 68 68"
                fill="none"
              >
                <rect width="68" height="68" rx="5" fill="#C2C2C2" />
              </svg>
              <div className={s.cardDescr}>
                <div className={s.cardDescrTitle}>Капучино</div>
                <div className={s.cardDescrAmount}>200 мл</div>
                <div className={s.cardDescrOptions}>+ овсяное молоко</div>
              </div>
            </div>

            <div className={s.price}>180 ₽</div>
          </div>
          <div className={s.card}>
            <div className={s.cardLeft}>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="68"
                height="68"
                viewBox="0 0 68 68"
                fill="none"
              >
                <rect width="68" height="68" rx="5" fill="#C2C2C2" />
              </svg>
              <div className={s.cardDescr}>
                <div className={s.cardDescrTitle}>Капучино</div>
                <div className={s.cardDescrAmount}>200 мл</div>
              </div>
            </div>

            <div className={s.price}>180 ₽</div>
          </div>
        </div>
      </div>

      <div className={s.bottom}>
        <div className={s.bottomTop}>
          <button className={s.addCardBtn}>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
            >
              <path
                d="M2 8.5H13.5M6 16.5H8M10.5 16.5H14.5"
                stroke="#828282"
                strokeWidth="1.5"
                strokeMiterlimit="10"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
              <path
                d="M22 12.03V16.11C22 19.62 21.11 20.5 17.56 20.5H6.44C2.89 20.5 2 19.62 2 16.11V7.89C2 4.38 2.89 3.5 6.44 3.5H13.5"
                stroke="#828282"
                strokeWidth="1.5"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
              <path
                d="M16.5 6.25H22M19.25 9V3.5"
                stroke="#828282"
                strokeWidth="1.5"
                strokeLinecap="round"
              />
            </svg>
            Добавить карту
          </button>
          <div className={s.commonPriceWrapper}>
            <div>Итого</div>
            <div className={s.commonPrice}>360 ₽</div>
          </div>
        </div>

        <button className={s.payBtn}>Оплатить</button>
      </div>
    </div>
  );
};

export default Order;
