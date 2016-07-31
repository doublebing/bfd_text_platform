# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `microBlog.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()

# Start of module com
_M_com = Ice.openModule('com')
__name__ = 'com'

# Start of module com.bfd
_M_com.bfd = Ice.openModule('com.bfd')
__name__ = 'com.bfd'

# Start of module com.bfd.crawler
_M_com.bfd.crawler = Ice.openModule('com.bfd.crawler')
__name__ = 'com.bfd.crawler'

if not _M_com.bfd.crawler.__dict__.has_key('weiboControl'):
    _M_com.bfd.crawler.weiboControl = Ice.createTempClass()
    class weiboControl(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_com.bfd.crawler.weiboControl:
                raise RuntimeError('com.bfd.crawler.weiboControl is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::com::bfd::crawler::weiboControl')

        def ice_id(self, current=None):
            return '::com::bfd::crawler::weiboControl'

        def ice_staticId():
            return '::com::bfd::crawler::weiboControl'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def addTask(self, request, current=None):
        # def queryTask(self, request, current=None):
        # def delTask(self, request, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_com.bfd.crawler._t_weiboControl)

        __repr__ = __str__

    _M_com.bfd.crawler.weiboControlPrx = Ice.createTempClass()
    class weiboControlPrx(Ice.ObjectPrx):

        def addTask(self, request, _ctx=None):
            return _M_com.bfd.crawler.weiboControl._op_addTask.invoke(self, ((request, ), _ctx))

        def queryTask(self, request, _ctx=None):
            return _M_com.bfd.crawler.weiboControl._op_queryTask.invoke(self, ((request, ), _ctx))

        def delTask(self, request, _ctx=None):
            return _M_com.bfd.crawler.weiboControl._op_delTask.invoke(self, ((request, ), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_com.bfd.crawler.weiboControlPrx.ice_checkedCast(proxy, '::com::bfd::crawler::weiboControl', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_com.bfd.crawler.weiboControlPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_com.bfd.crawler._t_weiboControlPrx = IcePy.defineProxy('::com::bfd::crawler::weiboControl', weiboControlPrx)

    _M_com.bfd.crawler._t_weiboControl = IcePy.defineClass('::com::bfd::crawler::weiboControl', weiboControl, (), True, None, (), ())
    weiboControl.ice_type = _M_com.bfd.crawler._t_weiboControl

    weiboControl._op_addTask = IcePy.Operation('addTask', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string),), (), IcePy._t_string, ())
    weiboControl._op_queryTask = IcePy.Operation('queryTask', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string),), (), IcePy._t_string, ())
    weiboControl._op_delTask = IcePy.Operation('delTask', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string),), (), IcePy._t_string, ())

    _M_com.bfd.crawler.weiboControl = weiboControl
    del weiboControl

    _M_com.bfd.crawler.weiboControlPrx = weiboControlPrx
    del weiboControlPrx

# End of module com.bfd.crawler

__name__ = 'com.bfd'

# End of module com.bfd

__name__ = 'com'

# End of module com
