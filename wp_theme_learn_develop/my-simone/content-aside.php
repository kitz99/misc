<?php
/**
 * @package my-simone
 */
?>

<article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
	<div class="index-box">
	<header class="entry-header">

		<?php 
			if(is_sticky()) {
				echo '<i class=" sticky-post fa fa-thumb-tack sticky-post"></i>';
			}
		?>

		<?php if ( 'post' == get_post_type() ) : ?>
		<?php endif; ?>
	</header><!-- .entry-header -->

	<div class="entry-content">
		<?php the_excerpt(); ?>
	</div><!-- .entry-content -->

	<footer class="entry-footer continue-reading">
		<div class="entry-meta">
			<?php my_simone_posted_on(); ?>
			<?php 
			    if ( ! post_password_required() && ( comments_open() || '0' != get_comments_number() ) ) { 
			        echo '<span class="comments-link">';
			        comments_popup_link( __( 'Leave a comment', 'my-simone' ), __( '1 Comment', 'my-simone' ), __( '% Comments', 'my-simone' ) );
			        echo '</span>';
			    }
			?>
			<?php edit_post_link( __( 'Edit', 'my-simone' ), '<span class="edit-link">', '</span>' ); ?>
		</div><!-- .entry-meta -->
	</footer><!-- .entry-footer -->
	</div>
</article><!-- #post-## -->
