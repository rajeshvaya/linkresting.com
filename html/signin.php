<?php include 'header.php' ?>
	
	<div class="container">
		<div class="row">
			<div class="col-md-4">
				<div class="login-container">
					<h2>Sign In</h2>
					<hr/>
					<form class="form-horizontal" role="" autocomplete="off">
				  	  <div class="form-group">
					    <label for="email" class="col-sm-3 control-label">Email</label>
					    <div class="col-sm-9">
					      <input type="email" class="form-control" id="login-email" placeholder="Email">
					    </div>
					  </div>

					  <div class="form-group">
					    <label for="password" class="col-sm-3 control-label">Password</label>
					    <div class="col-sm-9">
					      <input type="password" class="form-control" id="login-password" placeholder="Password">
					    </div>
					  </div>

					  <div class="form-group">
					    <div class="col-sm-offset-3 col-sm-9">
					      <button type="submit" class="btn btn-danger pull-left">Sign in</button> 
					      <span class='forgot-password pull-right'><small><a href="">Forgot password?</a></small></span>
					    </div>
					  </div>
					</form>
				</div><!-- login-container -->
			</div>
		</div><!-- row -->
	</div><!-- container -->

	<div class="container">
		<hr class="default-border"/>
	</div>
			
	<div class="container">
		<div class="row">
			<div class="col-md-4">
				<div class="register-container">
					<h2>Sign Up</h2>
					<hr/>
					<form class="form-horizontal" role="" autocomplete="off">
				  	  <div class="form-group">
					    <label for="name" class="col-sm-3 control-label">Name</label>
					    <div class="col-sm-9">
					      <input type="text" class="form-control" id="register-name" placeholder="Name">
					    </div>
					  </div>

				  	  <div class="form-group">
					    <label for="email" class="col-sm-3 control-label">Email</label>
					    <div class="col-sm-9">
					      <input type="email" class="form-control" id="register-email" placeholder="Email">
					    </div>
					  </div>

					  <div class="form-group">
					    <label for="password" class="col-sm-3 control-label">Password</label>
					    <div class="col-sm-9">
					      <input type="password" class="form-control" id="register-password" placeholder="Password">
					    </div>
					  </div>

					  <div class="form-group">
					    <div class="col-sm-offset-3 col-sm-10">
					      <button type="submit" class="btn btn-danger">Sign Up</button>
					    </div>
					  </div>
					</form>
				</div><!-- login-container -->
			</div>
		</div>
	</div>


<?php include 'footer.php' ?>