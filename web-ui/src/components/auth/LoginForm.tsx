import Link from "next/link";
import React from "react";

export default function LoginForm() {
  return (
    <form>
      <div className="form-control">
        <label className="label">
          <span className="label-text">Email</span>
        </label>
        <input
          type="email"
          placeholder="email"
          className="input input-bordered"
          required
        />
      </div>
      <div className="form-control">
        <label className="label">
          <span className="label-text">Password</span>
        </label>
        <input
          type="password"
          placeholder="password"
          className="input input-bordered"
          required
        />
        <label className="label">
          <a href="#" className="label-text-alt link link-hover">
            Forgot password?
          </a>
        </label>
      </div>
      <div className="form-control mt-6 gap-4">
        <button className="btn btn-primary">Login</button>

        <Link href="/auth/signup" className="link link-secondary">
          Create account
        </Link>
      </div>
    </form>
  );
}
