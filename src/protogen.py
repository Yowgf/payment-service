import glob
import logging
from os import getcwd
import sys

from grpc_tools import protoc

from common import log

logger = log.logger('protogen', logging.INFO)

proto_path = "src"
proto_files = glob.glob(proto_path + "/*.proto")
logger.info("Proto path: {}".format(proto_path))
logger.info("Proto files: {}".format(proto_files))

for proto_file in proto_files:
    args = (
        '-I{}'.format(proto_path),
        '--python_out={}'.format(proto_path),
        '--grpc_python_out={}'.format(proto_path),
        '--proto_path={}'.format(proto_path),
        proto_file,
    )
    logger.info("Running protoc with args: {}".format(args))
    protoc.main(args)
