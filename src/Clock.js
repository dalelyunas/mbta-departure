import React, { useEffect, useState } from 'react';

import styles from './Clock.module.css';

function Clock() {
    const [time, setTime] = useState(getLocalTime());

    useEffect(() => {
        const interval = setInterval(() => {
            setTime(getLocalTime())
        }, 1000);
        return () => clearInterval(interval);
      }, []);

    return (
        <div className={styles.container}>
            <div>{time.toDateString()}</div>
            <div>{time.toLocaleTimeString()}</div>
        </div>
    )
}

function getLocalTime() {
    return new Date();
}

export default Clock;