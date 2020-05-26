import React, { useEffect, useState } from 'react';

function Clock() {
    const [time, setTime] = useState(getLocalTime());

    useEffect(() => {
        const interval = setInterval(() => {
            setTime(getLocalTime())
        }, 1000);
        return () => clearInterval(interval);
      }, []);

    return (
        <div>{time}</div>
    )
}

function getLocalTime() {
    return new Date().toLocaleTimeString();
}

export default Clock;