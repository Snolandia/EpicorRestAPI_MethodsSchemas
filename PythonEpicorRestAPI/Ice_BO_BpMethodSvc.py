import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.BpMethodSvc
# Description: Manages BPM directives for customizing business object methods.
Contains BPM 4GL code generator for BPM directives.
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_BpMethods(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BpMethods items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BpMethods
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BpMethodRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpMethods",headers=creds) as resp:
           return await resp.json()

async def post_BpMethods(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BpMethods
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BpMethodRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BpMethodRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpMethods", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BpMethods_Source_BpMethodCode(Source, BpMethodCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BpMethod item
   Description: Calls GetByID to retrieve the BpMethod item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BpMethod
      :param Source: Desc: Source   Required: True   Allow empty value : True
      :param BpMethodCode: Desc: BpMethodCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BpMethodRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpMethods(" + Source + "," + BpMethodCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BpMethods_Source_BpMethodCode(Source, BpMethodCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BpMethod for the service
   Description: Calls UpdateExt to update BpMethod. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BpMethod
      :param Source: Desc: Source   Required: True   Allow empty value : True
      :param BpMethodCode: Desc: BpMethodCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BpMethodRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpMethods(" + Source + "," + BpMethodCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BpMethods_Source_BpMethodCode(Source, BpMethodCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BpMethod item
   Description: Call UpdateExt to delete BpMethod item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BpMethod
      :param Source: Desc: Source   Required: True   Allow empty value : True
      :param BpMethodCode: Desc: BpMethodCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpMethods(" + Source + "," + BpMethodCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_BpMethods_Source_BpMethodCode_BpArguments(Source, BpMethodCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BpArguments items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BpArguments1
      :param Source: Desc: Source   Required: True   Allow empty value : True
      :param BpMethodCode: Desc: BpMethodCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BpArgumentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpMethods(" + Source + "," + BpMethodCode + ")/BpArguments",headers=creds) as resp:
           return await resp.json()

async def get_BpMethods_Source_BpMethodCode_BpArguments_Source_BpMethodCode_Order(Source, BpMethodCode, Order, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BpArgument item
   Description: Calls GetByID to retrieve the BpArgument item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BpArgument1
      :param Source: Desc: Source   Required: True   Allow empty value : True
      :param BpMethodCode: Desc: BpMethodCode   Required: True   Allow empty value : True
      :param Order: Desc: Order   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BpArgumentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpMethods(" + Source + "," + BpMethodCode + ")/BpArguments(" + Source + "," + BpMethodCode + "," + Order + ")",headers=creds) as resp:
           return await resp.json()

async def get_BpMethods_Source_BpMethodCode_BpDirectives(Source, BpMethodCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BpDirectives items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BpDirectives1
      :param Source: Desc: Source   Required: True   Allow empty value : True
      :param BpMethodCode: Desc: BpMethodCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BpDirectiveRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpMethods(" + Source + "," + BpMethodCode + ")/BpDirectives",headers=creds) as resp:
           return await resp.json()

async def get_BpMethods_Source_BpMethodCode_BpDirectives_DirectiveID(Source, BpMethodCode, DirectiveID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BpDirective item
   Description: Calls GetByID to retrieve the BpDirective item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BpDirective1
      :param Source: Desc: Source   Required: True   Allow empty value : True
      :param BpMethodCode: Desc: BpMethodCode   Required: True   Allow empty value : True
      :param DirectiveID: Desc: DirectiveID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BpDirectiveRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpMethods(" + Source + "," + BpMethodCode + ")/BpDirectives(" + DirectiveID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BpArguments(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BpArguments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BpArguments
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BpArgumentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpArguments",headers=creds) as resp:
           return await resp.json()

async def post_BpArguments(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BpArguments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BpArgumentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BpArgumentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpArguments", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BpArguments_Source_BpMethodCode_Order(Source, BpMethodCode, Order, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BpArgument item
   Description: Calls GetByID to retrieve the BpArgument item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BpArgument
      :param Source: Desc: Source   Required: True   Allow empty value : True
      :param BpMethodCode: Desc: BpMethodCode   Required: True   Allow empty value : True
      :param Order: Desc: Order   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BpArgumentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpArguments(" + Source + "," + BpMethodCode + "," + Order + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BpArguments_Source_BpMethodCode_Order(Source, BpMethodCode, Order, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BpArgument for the service
   Description: Calls UpdateExt to update BpArgument. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BpArgument
      :param Source: Desc: Source   Required: True   Allow empty value : True
      :param BpMethodCode: Desc: BpMethodCode   Required: True   Allow empty value : True
      :param Order: Desc: Order   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BpArgumentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpArguments(" + Source + "," + BpMethodCode + "," + Order + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BpArguments_Source_BpMethodCode_Order(Source, BpMethodCode, Order, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BpArgument item
   Description: Call UpdateExt to delete BpArgument item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BpArgument
      :param Source: Desc: Source   Required: True   Allow empty value : True
      :param BpMethodCode: Desc: BpMethodCode   Required: True   Allow empty value : True
      :param Order: Desc: Order   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpArguments(" + Source + "," + BpMethodCode + "," + Order + ")",headers=creds) as resp:
           return await resp.json()

async def get_BpDirectives(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BpDirectives items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BpDirectives
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BpDirectiveRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpDirectives",headers=creds) as resp:
           return await resp.json()

async def post_BpDirectives(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BpDirectives
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BpDirectiveRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BpDirectiveRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpDirectives", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BpDirectives_DirectiveID(DirectiveID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BpDirective item
   Description: Calls GetByID to retrieve the BpDirective item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BpDirective
      :param DirectiveID: Desc: DirectiveID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BpDirectiveRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpDirectives(" + DirectiveID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BpDirectives_DirectiveID(DirectiveID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BpDirective for the service
   Description: Calls UpdateExt to update BpDirective. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BpDirective
      :param DirectiveID: Desc: DirectiveID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BpDirectiveRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpDirectives(" + DirectiveID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BpDirectives_DirectiveID(DirectiveID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BpDirective item
   Description: Call UpdateExt to delete BpDirective item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BpDirective
      :param DirectiveID: Desc: DirectiveID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpDirectives(" + DirectiveID + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BpMethodListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseBpMethod, whereClauseBpArgument, whereClauseBpDirective, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBpMethod=" + whereClauseBpMethod
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBpArgument=" + whereClauseBpArgument
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBpDirective=" + whereClauseBpDirective
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(source, bpMethodCode, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "source=" + source
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "bpMethodCode=" + bpMethodCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_DeleteDirectiveGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteDirectiveGroup
   Description: Deletes directives by group name for business objects and data tables. UBAQ directives are not involved in this process
   OperationID: DeleteDirectiveGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteDirectiveGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteDirectiveGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailableReferences(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailableReferences
   Description: Gets the available references.
   OperationID: GetAvailableReferences
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailableReferences_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableReferences_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPagedAvailableReferences(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPagedAvailableReferences
   Description: Gets the available references.
   OperationID: GetPagedAvailableReferences
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPagedAvailableReferences_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPagedAvailableReferences_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMethodsByDirectiveGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMethodsByDirectiveGroup
   Description: Gets list of methods which have directives belong to specified directive group.
   OperationID: GetMethodsByDirectiveGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMethodsByDirectiveGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMethodsByDirectiveGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMethodsByDirectiveGroupAndSCCredentials(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMethodsByDirectiveGroupAndSCCredentials
   Description: Gets list of methods which have directives belong to specified directive group and contain SC action with specified SC credentials.
   OperationID: GetMethodsByDirectiveGroupAndSCCredentials
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMethodsByDirectiveGroupAndSCCredentials_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMethodsByDirectiveGroupAndSCCredentials_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMethodsByDirectiveFlags(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMethodsByDirectiveFlags
   Description: Gets list of methods which have directives with specified flags
   OperationID: GetMethodsByDirectiveFlags
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMethodsByDirectiveFlags_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMethodsByDirectiveFlags_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDirectiveGroups(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDirectiveGroups
   Description: Gets the directive groups.
   OperationID: GetDirectiveGroups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDirectiveGroups_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDirectiveGroups_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetEntityList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetEntityList
   Description: Gets the entity list.
   OperationID: GetEntityList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEntityList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEntityList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMatchedClasses(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMatchedClasses
   Description: Gets the matched classes.
   OperationID: GetMatchedClasses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMatchedClasses_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMatchedClasses_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMatchedTypes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMatchedTypes
   Description: Gets the matched types.
   OperationID: GetMatchedTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMatchedTypes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMatchedTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBpDirectiveEx(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBpDirectiveEx
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBpDirectiveEx
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBpDirectiveEx_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBpDirectiveEx_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsEx(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsEx
   OperationID: GetRowsEx
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsEx_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsEx_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportMethod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportMethod
   Description: Imports the method's directives into the current company.
   OperationID: ImportMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InvalidateCaches(epicorHeaders = None):
   """  
   Summary: Invoke method InvalidateCaches
   Description: Invalidate services specific caches.
   OperationID: InvalidateCaches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/InvalidateCaches_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_PrepareArguments(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrepareArguments
   Description: Gets the method arguments.
   OperationID: PrepareArguments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrepareArguments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrepareArguments_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrepareTriggerDefinitions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrepareTriggerDefinitions
   Description: Prepares the trigger definitions.
   OperationID: PrepareTriggerDefinitions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrepareTriggerDefinitions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrepareTriggerDefinitions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RegisterMethodCustomization(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RegisterMethodCustomization
   Description: Creates or updated Service Method customization entry.
Method returns Method Codes of registered entries (e.g., "Ice.BO.Tip.Update")
   OperationID: RegisterMethodCustomization
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RegisterMethodCustomization_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RegisterMethodCustomization_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateDirectivesByMethod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateDirectivesByMethod
   Description: Updates all directives belong to specified method according to settings in DirectiveUpdateInfo
   OperationID: UpdateDirectivesByMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateDirectivesByMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateDirectivesByMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateMethod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateMethod
   Description: Validates the method.
   OperationID: ValidateMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateUserCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateUserCode
   Description: Validates the user code.
   OperationID: ValidateUserCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateUserCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateUserCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDirectivesForMethodsCollection(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDirectivesForMethodsCollection
   Description: Get all available directives for particular methods
   OperationID: GetDirectivesForMethodsCollection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDirectivesForMethodsCollection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDirectivesForMethodsCollection_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportByDirectiveGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportByDirectiveGroup
   Description: Exports directives by group.
   OperationID: ExportByDirectiveGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportByDirectiveGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportByDirectiveGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportByService(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportByService
   Description: Exports directives by service.
   OperationID: ExportByService
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportByService_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportByService_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportByTable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportByTable
   Description: Exports directives by table.
   OperationID: ExportByTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportByTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportByTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Import(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Import
   Description: Imports directives.
   OperationID: Import
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Import_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Import_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportBySource(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportBySource
   Description: Imports directives by source.
   OperationID: ImportBySource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportBySource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportBySource_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ShallowValidate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ShallowValidate
   Description: Validates that the data selected for import appears valid.
   OperationID: ShallowValidate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ShallowValidate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ShallowValidate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBpmDirectiveGroupsTS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBpmDirectiveGroupsTS
   Description: Get BPM Directive groups as typed tableset.
   OperationID: GetBpmDirectiveGroupsTS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBpmDirectiveGroupsTS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBpmDirectiveGroupsTS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBpMethod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBpMethod
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBpMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBpMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBpMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBpArgument(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBpArgument
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBpArgument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBpArgument_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBpArgument_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBpDirective(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBpDirective
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBpDirective
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBpDirective_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBpDirective_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDirectiveVariableTypes(epicorHeaders = None):
   """  
   Summary: Invoke method GetDirectiveVariableTypes
   Description: Returns a list of available directive variable types
   OperationID: GetDirectiveVariableTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDirectiveVariableTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetByIDBpMethod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIDBpMethod
   OperationID: GetByIDBpMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDBpMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDBpMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetKineticDirective(directiveId, epicorHeaders = None):
   """  
   Summary: Invoke method GetKineticDirective
   Description: Get XAML directive transformed into JSON for Kinetic browser UI.
   OperationID: Get_GetKineticDirective
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetKineticDirective_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "directiveId=" + directiveId

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetTablesetRelations(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTablesetRelations
   Description: Get tableset relations for execution rules.
   OperationID: GetTablesetRelations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTablesetRelations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTablesetRelations_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreProcessExpression(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreProcessExpression
   Description: Prepare table parameters for the expression.
   OperationID: PreProcessExpression
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreProcessExpression_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreProcessExpression_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateExpression(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateExpression
   Description: Validate expression.
   OperationID: ValidateExpression
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateExpression_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateExpression_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateCustomCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCustomCode
   Description: Validate custom code.
   OperationID: ValidateCustomCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCustomCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCustomCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsValidIdentifier(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsValidIdentifier
   Description: Verify variable name.
   OperationID: IsValidIdentifier
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsValidIdentifier_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsValidIdentifier_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailableReferencesWithFilter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailableReferencesWithFilter
   Description: Gets the available references.
   OperationID: GetAvailableReferencesWithFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailableReferencesWithFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableReferencesWithFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFoldersForExternalAssemblies(epicorHeaders = None):
   """  
   Summary: Invoke method GetFoldersForExternalAssemblies
   Description: Get external assembly directory.
   OperationID: GetFoldersForExternalAssemblies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFoldersForExternalAssemblies_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ValidateKineticDirective(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateKineticDirective
   Description: Validate directive from Kinetic browser UI.
   OperationID: ValidateKineticDirective
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateKineticDirective_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateKineticDirective_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GeneratePICode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GeneratePICode
   Description: Generates the Programming Interface code.
   OperationID: GeneratePICode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GeneratePICode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GeneratePICode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetDirectiveLandingPageList(source, group, whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetDirectiveLandingPageList
   Description: Get list of directives to show on landing page.
   OperationID: Get_GetDirectiveLandingPageList
      :param source: Desc: Directive source.   Required: True   Allow empty value : True
      :param group: Desc: Directive group or empty value.   Required: True   Allow empty value : True
      :param whereClause: Desc: Filtering and sorting.   Required: True   Allow empty value : True
      :param pageSize: Desc: Page size.   Required: True
      :param absolutePage: Desc: Page to show.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDirectiveLandingPageList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "source=" + source
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "group=" + group
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_PrepareAndSearchMethodRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrepareAndSearchMethodRows
   OperationID: PrepareAndSearchMethodRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrepareAndSearchMethodRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrepareAndSearchMethodRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetWidgets(epicorHeaders = None):
   """  
   Summary: Invoke method GetWidgets
   Description: Get list of BPM widgets.
   OperationID: Get_GetWidgets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWidgets_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BpArgumentRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_BpArgumentRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BpDirectiveRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_BpDirectiveRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BpMethodListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_BpMethodListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BpMethodRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_BpMethodRow] = obj["value"]
      pass

class Ice_Tablesets_BpArgumentRow:
   def __init__(self, obj):
      self.Source:str = obj["Source"]
      """  BPM Agument Source  """  
      self.BpMethodCode:str = obj["BpMethodCode"]
      """  BPM customization target ID  """  
      self.Order:int = obj["Order"]
      """  BPM Argument Order sequence number  """  
      self.BpArgumentName:str = obj["BpArgumentName"]
      """  BPM Argument Name  """  
      self.Type:str = obj["Type"]
      """  BPM Argument Type  """  
      self.Direction:str = obj["Direction"]
      """  BPM Argument Direction: input, output  """  
      self.TypeInfo:str = obj["TypeInfo"]
      """  TypeInfo  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BpDirectiveRow:
   def __init__(self, obj):
      self.DirectiveID:str = obj["DirectiveID"]
      """  DirectiveID  """  
      self.Source:str = obj["Source"]
      """  Source  """  
      self.BpMethodCode:str = obj["BpMethodCode"]
      """  BPM customization target ID  """  
      self.DirectiveType:int = obj["DirectiveType"]
      """  BPM directive type  """  
      self.Name:str = obj["Name"]
      """  Name  """  
      self.Order:int = obj["Order"]
      """  Order  """  
      self.IsEnabled:bool = obj["IsEnabled"]
      """  IsEnabled  """  
      self.ReenterMax:int = obj["ReenterMax"]
      """  ReenterMax  """  
      self.PreventDeadloops:bool = obj["PreventDeadloops"]
      """  PreventDeadloops  """  
      self.VisibilityScope:int = obj["VisibilityScope"]
      """  VisibilityScope  """  
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DirectiveGroup:str = obj["DirectiveGroup"]
      """  DirectiveGroup  """  
      self.IsUpToDate:bool = obj["IsUpToDate"]
      """  IsUpToDate  """  
      self.CGCCode:str = obj["CGCCode"]
      """  CGCCode  """  
      self.Body:str = obj["Body"]
      """  Body  """  
      self.Thumbnail:str = obj["Thumbnail"]
      """  Thumbnail  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DisplayOrder:int = obj["DisplayOrder"]
      """  external column to sort directives in the UI.   Equal to Order but allows to change Order value on UI without resorting dataview  """  
      self.CompilerDiagnostics:str = obj["CompilerDiagnostics"]
      """  The compiler diagnostics if a compilation was done.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BpMethodListRow:
   def __init__(self, obj):
      self.Source:str = obj["Source"]
      """  BPM source  """  
      self.BpMethodCode:str = obj["BpMethodCode"]
      """  BPM customization target ID  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ObjectNS:str = obj["ObjectNS"]
      """  ObjectNS  """  
      self.BusinessObject:str = obj["BusinessObject"]
      """  Referenced Business Object  """  
      self.Name:str = obj["Name"]
      """  BPM Method Name  """  
      self.Description:str = obj["Description"]
      """  BPM Method Description  """  
      self.Version:str = obj["Version"]
      """  Version  """  
      self.HasRootTransaction:bool = obj["HasRootTransaction"]
      """  Root Transaction flag  """  
      self.SignatureStatus:int = obj["SignatureStatus"]
      """  SignatureStatus  """  
      self.Disabled:bool = obj["Disabled"]
      """  BPM Method customization's enable/disable flag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HasOutdatedDirectives:bool = obj["HasOutdatedDirectives"]
      self.HasPreProcessing:bool = obj["HasPreProcessing"]
      self.HasBaseProcessing:bool = obj["HasBaseProcessing"]
      self.HasPostProcessing:bool = obj["HasPostProcessing"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BpMethodRow:
   def __init__(self, obj):
      self.Source:str = obj["Source"]
      """  BPM source  """  
      self.BpMethodCode:str = obj["BpMethodCode"]
      """  BPM customization target ID  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ObjectNS:str = obj["ObjectNS"]
      """  ObjectNS  """  
      self.BusinessObject:str = obj["BusinessObject"]
      """  Referenced Business Object  """  
      self.Name:str = obj["Name"]
      """  BPM Method Name  """  
      self.Description:str = obj["Description"]
      """  BPM Method Description  """  
      self.Version:str = obj["Version"]
      """  Version  """  
      self.HasRootTransaction:bool = obj["HasRootTransaction"]
      """  Root Transaction flag  """  
      self.SignatureStatus:int = obj["SignatureStatus"]
      """  SignatureStatus  """  
      self.Disabled:bool = obj["Disabled"]
      """  BPM Method customization's enable/disable flag  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DebugMode:bool = obj["DebugMode"]
      """  DebugMode  """  
      self.DumpSources:bool = obj["DumpSources"]
      """  DumpSources  """  
      self.AdvTracing:bool = obj["AdvTracing"]
      """  AdvTracing  """  
      self.HasOutdatedDirectives:bool = obj["HasOutdatedDirectives"]
      self.HasPreProcessing:bool = obj["HasPreProcessing"]
      self.HasBaseProcessing:bool = obj["HasBaseProcessing"]
      self.HasPostProcessing:bool = obj["HasPostProcessing"]
      self.IsMDRSEnabled:bool = obj["IsMDRSEnabled"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   source
   bpMethodCode
   """  
   def __init__(self, obj):
      self.source:str = obj["source"]
      self.bpMethodCode:str = obj["bpMethodCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteDirectiveGroup_input:
   """ Required : 
   anyGroup
   directiveGroup
   """  
   def __init__(self, obj):
      self.anyGroup:bool = obj["anyGroup"]
      """  if set to `true` [any group].  """  
      self.directiveGroup:str = obj["directiveGroup"]
      """  The directive group.  """  
      pass

class DeleteDirectiveGroup_output:
   def __init__(self, obj):
      pass

class Epicor_Customization_CodeCheckResult:
   def __init__(self, obj):
      self.diagnostics:list[Epicor_Customization_CodeDiagnostic] = obj["diagnostics"]
      pass

class Epicor_Customization_CodeDiagnostic:
   def __init__(self, obj):
      self.Severity:int = obj["Severity"]
      self.Code:str = obj["Code"]
      self.Message:str = obj["Message"]
      self.File:str = obj["File"]
      self.Span:list[Epicor_Customization_LineSpan] = obj["Span"]
      pass

class Epicor_Customization_LinePosition:
   def __init__(self, obj):
      self.line:int = obj["line"]
      self.column:int = obj["column"]
      pass

class Epicor_Customization_LineSpan:
   def __init__(self, obj):
      self.start:list[Epicor_Customization_LinePosition] = obj["start"]
      self.end:list[Epicor_Customization_LinePosition] = obj["end"]
      pass

class Epicor_Customization_Metadata_TypeRef:
   def __init__(self, obj):
      self.wellknownType:int = obj["wellknownType"]
      self.namespace:str = obj["namespace"]
      self.name:str = obj["name"]
      self.assembly:str = obj["assembly"]
      self.options:int = obj["options"]
      self.elementType:list[Epicor_Customization_Metadata_TypeRef] = obj["elementType"]
      self.genericArguments:list[Epicor_Customization_Metadata_TypeRef] = obj["genericArguments"]
      pass

class ExportByDirectiveGroup_input:
   """ Required : 
   groupName
   """  
   def __init__(self, obj):
      self.groupName:str = obj["groupName"]
      pass

class ExportByDirectiveGroup_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BO_BpMethod_DirectiveExportResult] = obj["returnObj"]
      pass

class ExportByService_input:
   """ Required : 
   systemCode
   serviceKind
   serviceName
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      self.serviceKind:str = obj["serviceKind"]
      self.serviceName:str = obj["serviceName"]
      pass

class ExportByService_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BO_BpMethod_DirectiveExportResult] = obj["returnObj"]
      pass

class ExportByTable_input:
   """ Required : 
   systemCode
   tableName
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      self.tableName:str = obj["tableName"]
      pass

class ExportByTable_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BO_BpMethod_DirectiveExportResult] = obj["returnObj"]
      pass

class GeneratePICode_input:
   """ Required : 
   ds
   dotNetLanguage
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BpMethodTableset] = obj["ds"]
      self.dotNetLanguage:str = obj["dotNetLanguage"]
      """  The dot net language. For example: CSharp, VbNet.  """  
      pass

class GeneratePICode_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The generated code.  """  
      pass

class GetAvailableReferencesWithFilter_input:
   """ Required : 
   referenceGroup
   filter
   pageNum
   pageSize
   """  
   def __init__(self, obj):
      self.referenceGroup:str = obj["referenceGroup"]
      """  The reference group.  """  
      self.filter:str = obj["filter"]
      """  Search filter. If empty, * will be used.  """  
      self.pageNum:int = obj["pageNum"]
      """  Page number starting 1/  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size between 1 and 50.  """  
      pass

class GetAvailableReferencesWithFilter_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Contracts_BO_BpMethod_ReferenceInfo] = obj["returnObj"]
      """  List of assembly names for specific filter/  """  
      pass

class GetAvailableReferences_input:
   """ Required : 
   referenceGroup
   """  
   def __init__(self, obj):
      self.referenceGroup:str = obj["referenceGroup"]
      """  The reference group.  """  
      pass

class GetAvailableReferences_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Contracts_BO_BpMethod_ReferenceInfo] = obj["returnObj"]
      pass

class GetBpmDirectiveGroupsTS_input:
   """ Required : 
   includeUndefined
   includeAny
   """  
   def __init__(self, obj):
      self.includeUndefined:bool = obj["includeUndefined"]
      """  include undefined.  """  
      self.includeAny:bool = obj["includeAny"]
      """  include any.  """  
      pass

class GetBpmDirectiveGroupsTS_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BpDirectiveGroupTableset] = obj["returnObj"]
      pass

class GetByIDBpMethod_input:
   """ Required : 
   source
   bpMethodCode
   """  
   def __init__(self, obj):
      self.source:str = obj["source"]
      self.bpMethodCode:str = obj["bpMethodCode"]
      pass

class GetByIDBpMethod_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BpMethodTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   source
   bpMethodCode
   """  
   def __init__(self, obj):
      self.source:str = obj["source"]
      self.bpMethodCode:str = obj["bpMethodCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BpMethodTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BpMethodTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BpMethodTableset] = obj["returnObj"]
      pass

class GetDirectiveGroups_input:
   """ Required : 
   sources
   """  
   def __init__(self, obj):
      self.sources:str = obj["sources"]
      """  The sources.  """  
      pass

class GetDirectiveGroups_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetDirectiveLandingPageList_input:
   """ Required : 
   source
   group
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.source:str = obj["source"]
      """  Directive source.  """  
      self.group:str = obj["group"]
      """  Directive group or empty value.  """  
      self.whereClause:str = obj["whereClause"]
      """  Filtering and sorting.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page to show.  """  
      pass

class GetDirectiveLandingPageList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BpMethodListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetDirectiveVariableTypes_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetDirectivesForMethodsCollection_input:
   """ Required : 
   boSource
   methods
   """  
   def __init__(self, obj):
      self.boSource:str = obj["boSource"]
      """  The source.  """  
      self.methods:str = obj["methods"]
      """  List of methods.  """  
      pass

class GetDirectivesForMethodsCollection_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BpDirectiveRow] = obj["returnObj"]
      """  List of directives designed for selected methods  """  
      pass

class GetEntityList_input:
   """ Required : 
   source
   filter
   withDirectivesOnly
   """  
   def __init__(self, obj):
      self.source:str = obj["source"]
      """  The source type (one of "BO", "DB", "DQ").  """  
      self.filter:int = obj["filter"]
      self.withDirectivesOnly:bool = obj["withDirectivesOnly"]
      """  True if entities should be filtered by presence of linked directives  """  
      pass

class GetEntityList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Contracts_BpmEntity] = obj["returnObj"]
      pass

class GetFoldersForExternalAssemblies_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetKineticDirective_input:
   """ Required : 
   directiveId
   """  
   def __init__(self, obj):
      self.directiveId:str = obj["directiveId"]
      pass

class GetKineticDirective_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Directive serialized in JSON.  """  
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BpMethodListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetMatchedClasses_input:
   """ Required : 
   assemblyId
   matchToMethod
   methodSource
   """  
   def __init__(self, obj):
      self.assemblyId:str = obj["assemblyId"]
      """  The assembly id.  """  
      self.matchToMethod:str = obj["matchToMethod"]
      """  The match to method.  """  
      self.methodSource:str = obj["methodSource"]
      """  The match to method source.  """  
      pass

class GetMatchedClasses_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Contracts_BO_BpMethod_ClassInfo] = obj["returnObj"]
      pass

class GetMatchedTypes_input:
   """ Required : 
   assemblyId
   baseType
   typeStartsWith
   typeEndsWith
   """  
   def __init__(self, obj):
      self.assemblyId:str = obj["assemblyId"]
      """  The assembly id.  """  
      self.baseType:str = obj["baseType"]
      """  Searchable class must have this base type  """  
      self.typeStartsWith:str = obj["typeStartsWith"]
      """  Searchable class name starts with...  """  
      self.typeEndsWith:str = obj["typeEndsWith"]
      """  Searchable class name ends with...  """  
      pass

class GetMatchedTypes_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetMethodsByDirectiveFlags_input:
   """ Required : 
   directivesState
   boSource
   directivesScope
   visibilityScopes
   """  
   def __init__(self, obj):
      self.directivesState:int = obj["directivesState"]
      """  State of directives to find  """  
      self.boSource:str = obj["boSource"]
      """  if set to `BO` then selects methods which have source is BO. If set to `DB` then selects methods which have source is DB. If set to empty then selects all methods except DQ  """  
      self.directivesScope:int = obj["directivesScope"]
      """  Scope of directives to find  """  
      self.visibilityScopes:int = obj["visibilityScopes"]
      """  Sets of visibility scopes of directives to find  """  
      pass

class GetMethodsByDirectiveFlags_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BpMethodListTableset] = obj["returnObj"]
      pass

class GetMethodsByDirectiveGroupAndSCCredentials_input:
   """ Required : 
   directiveGroup
   credentials
   """  
   def __init__(self, obj):
      self.directiveGroup:str = obj["directiveGroup"]
      """  The directive group. `Null` value means don't filter by directive group  """  
      self.credentials:list[Ice_Contracts_BO_BpMethod_EscCredentialsUpdateInfo] = obj["credentials"]
      pass

class GetMethodsByDirectiveGroupAndSCCredentials_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BpMethodListTableset] = obj["returnObj"]
      pass

class GetMethodsByDirectiveGroup_input:
   """ Required : 
   directiveGroup
   """  
   def __init__(self, obj):
      self.directiveGroup:str = obj["directiveGroup"]
      """  The directive group.  """  
      pass

class GetMethodsByDirectiveGroup_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BpMethodListTableset] = obj["returnObj"]
      pass

class GetNewBpArgument_input:
   """ Required : 
   ds
   source
   bpMethodCode
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BpMethodTableset] = obj["ds"]
      self.source:str = obj["source"]
      self.bpMethodCode:str = obj["bpMethodCode"]
      pass

class GetNewBpArgument_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BpMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBpDirectiveEx_input:
   """ Required : 
   ds
   source
   bpMethodCode
   directiveType
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BpMethodTableset] = obj["ds"]
      self.source:str = obj["source"]
      self.bpMethodCode:str = obj["bpMethodCode"]
      self.directiveType:int = obj["directiveType"]
      pass

class GetNewBpDirectiveEx_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BpMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBpDirective_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BpMethodTableset] = obj["ds"]
      pass

class GetNewBpDirective_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BpMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBpMethod_input:
   """ Required : 
   ds
   source
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BpMethodTableset] = obj["ds"]
      self.source:str = obj["source"]
      pass

class GetNewBpMethod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BpMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPagedAvailableReferences_input:
   """ Required : 
   referenceGroup
   pageNum
   pageSize
   """  
   def __init__(self, obj):
      self.referenceGroup:str = obj["referenceGroup"]
      """  The reference group.  """  
      self.pageNum:int = obj["pageNum"]
      """  Page number  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size  """  
      pass

class GetPagedAvailableReferences_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Contracts_BO_BpMethod_ReferenceInfo] = obj["returnObj"]
      pass

class GetRowsEx_input:
   """ Required : 
   source
   whereClauseBpMethod
   whereClauseBpDirective
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.source:str = obj["source"]
      self.whereClauseBpMethod:str = obj["whereClauseBpMethod"]
      self.whereClauseBpDirective:str = obj["whereClauseBpDirective"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsEx_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BpMethodTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseBpMethod
   whereClauseBpArgument
   whereClauseBpDirective
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseBpMethod:str = obj["whereClauseBpMethod"]
      self.whereClauseBpArgument:str = obj["whereClauseBpArgument"]
      self.whereClauseBpDirective:str = obj["whereClauseBpDirective"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BpMethodTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTablesetRelations_input:
   """ Required : 
   primaryTable
   tableSetParameters
   isDqMethod
   """  
   def __init__(self, obj):
      self.primaryTable:str = obj["primaryTable"]
      """  Selected primary table.  """  
      self.tableSetParameters      #schema had no properties on an object.
      """  List of parameters with tableset types.  """  
      self.isDqMethod:bool = obj["isDqMethod"]
      """  If is called for UBAQ.  """  
      pass

class GetTablesetRelations_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Serialized tableset relations.  """  
      pass

class GetWidgets_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BpWidgetsTableset] = obj["returnObj"]
      pass

class Ice_BO_BpMethod_DirectiveExportImportResult:
   def __init__(self, obj):
      self.Log:str = obj["Log"]
      self.HasErrors:bool = obj["HasErrors"]
      pass

class Ice_BO_BpMethod_DirectiveExportResult:
   def __init__(self, obj):
      self.Data:str = obj["Data"]
      self.Log:str = obj["Log"]
      self.HasErrors:bool = obj["HasErrors"]
      pass

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Contracts_BO_BpMethod_ClassInfo:
   def __init__(self, obj):
      self.Name:str = obj["Name"]
      self.RequiresDbContext:bool = obj["RequiresDbContext"]
      self.Methods:list[System_Tuple_System_String_System_Boolean] = obj["Methods"]
      self.StaticMethods:list[System_Tuple_System_String_System_Boolean] = obj["StaticMethods"]
      pass

class Ice_Contracts_BO_BpMethod_DirectiveCompileError:
   def __init__(self, obj):
      self.DirectiveID:str = obj["DirectiveID"]
      self.DirectiveName:str = obj["DirectiveName"]
      self.DirectiveType:str = obj["DirectiveType"]
      self.CompileError:str = obj["CompileError"]
      self.Company:str = obj["Company"]
      pass

class Ice_Contracts_BO_BpMethod_DirectiveUpdateInfo:
   def __init__(self, obj):
      self.GroupName:str = obj["GroupName"]
      self.NewGroupName:str = obj["NewGroupName"]
      self.SetEnabled:bool = obj["SetEnabled"]
      self.SetVisibilityScope:int = obj["SetVisibilityScope"]
      self.SetPreventEndlessLoops:bool = obj["SetPreventEndlessLoops"]
      self.ReenterMax:int = obj["ReenterMax"]
      self.Process:int = obj["Process"]
      self.DirectivesState:int = obj["DirectivesState"]
      self.RegenerateMethodSignature:bool = obj["RegenerateMethodSignature"]
      self.EscCredentialsToSearch:list[Ice_Contracts_BO_BpMethod_EscCredentialsUpdateInfo] = obj["EscCredentialsToSearch"]
      self.EscCredentialsToUpdate:list[Ice_Contracts_BO_BpMethod_EscCredentialsUpdateInfo] = obj["EscCredentialsToUpdate"]
      self.DirectivesScope:int = obj["DirectivesScope"]
      self.DirectivesVisibilityScopes:int = obj["DirectivesVisibilityScopes"]
      pass

class Ice_Contracts_BO_BpMethod_EscCredentialsUpdateInfo:
   def __init__(self, obj):
      self.ServerNameType:int = obj["ServerNameType"]
      self.ServerName:str = obj["ServerName"]
      self.UserType:int = obj["UserType"]
      self.User:str = obj["User"]
      self.Password:str = obj["Password"]
      pass

class Ice_Contracts_BO_BpMethod_ReferenceInfo:
   def __init__(self, obj):
      self.Name:str = obj["Name"]
      self.FileName:str = obj["FileName"]
      self.Version:str = obj["Version"]
      pass

class Ice_Contracts_BpmEntity:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      self.Name:str = obj["Name"]
      self.Type:int = obj["Type"]
      self.Description:str = obj["Description"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class Ice_Tablesets_BpArgumentRow:
   def __init__(self, obj):
      self.Source:str = obj["Source"]
      """  BPM Agument Source  """  
      self.BpMethodCode:str = obj["BpMethodCode"]
      """  BPM customization target ID  """  
      self.Order:int = obj["Order"]
      """  BPM Argument Order sequence number  """  
      self.BpArgumentName:str = obj["BpArgumentName"]
      """  BPM Argument Name  """  
      self.Type:str = obj["Type"]
      """  BPM Argument Type  """  
      self.Direction:str = obj["Direction"]
      """  BPM Argument Direction: input, output  """  
      self.TypeInfo:str = obj["TypeInfo"]
      """  TypeInfo  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BpDirectiveGroupRow:
   def __init__(self, obj):
      self.GroupID:int = obj["GroupID"]
      """  Directive group identifier.  """  
      self.GroupName:str = obj["GroupName"]
      """  Directive group name.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BpDirectiveGroupTableset:
   def __init__(self, obj):
      self.BpDirectiveGroup:list[Ice_Tablesets_BpDirectiveGroupRow] = obj["BpDirectiveGroup"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_BpDirectiveRow:
   def __init__(self, obj):
      self.DirectiveID:str = obj["DirectiveID"]
      """  DirectiveID  """  
      self.Source:str = obj["Source"]
      """  Source  """  
      self.BpMethodCode:str = obj["BpMethodCode"]
      """  BPM customization target ID  """  
      self.DirectiveType:int = obj["DirectiveType"]
      """  BPM directive type  """  
      self.Name:str = obj["Name"]
      """  Name  """  
      self.Order:int = obj["Order"]
      """  Order  """  
      self.IsEnabled:bool = obj["IsEnabled"]
      """  IsEnabled  """  
      self.ReenterMax:int = obj["ReenterMax"]
      """  ReenterMax  """  
      self.PreventDeadloops:bool = obj["PreventDeadloops"]
      """  PreventDeadloops  """  
      self.VisibilityScope:int = obj["VisibilityScope"]
      """  VisibilityScope  """  
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DirectiveGroup:str = obj["DirectiveGroup"]
      """  DirectiveGroup  """  
      self.IsUpToDate:bool = obj["IsUpToDate"]
      """  IsUpToDate  """  
      self.CGCCode:str = obj["CGCCode"]
      """  CGCCode  """  
      self.Body:str = obj["Body"]
      """  Body  """  
      self.Thumbnail:str = obj["Thumbnail"]
      """  Thumbnail  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DisplayOrder:int = obj["DisplayOrder"]
      """  external column to sort directives in the UI.   Equal to Order but allows to change Order value on UI without resorting dataview  """  
      self.CompilerDiagnostics:str = obj["CompilerDiagnostics"]
      """  The compiler diagnostics if a compilation was done.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BpMethodListRow:
   def __init__(self, obj):
      self.Source:str = obj["Source"]
      """  BPM source  """  
      self.BpMethodCode:str = obj["BpMethodCode"]
      """  BPM customization target ID  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ObjectNS:str = obj["ObjectNS"]
      """  ObjectNS  """  
      self.BusinessObject:str = obj["BusinessObject"]
      """  Referenced Business Object  """  
      self.Name:str = obj["Name"]
      """  BPM Method Name  """  
      self.Description:str = obj["Description"]
      """  BPM Method Description  """  
      self.Version:str = obj["Version"]
      """  Version  """  
      self.HasRootTransaction:bool = obj["HasRootTransaction"]
      """  Root Transaction flag  """  
      self.SignatureStatus:int = obj["SignatureStatus"]
      """  SignatureStatus  """  
      self.Disabled:bool = obj["Disabled"]
      """  BPM Method customization's enable/disable flag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HasOutdatedDirectives:bool = obj["HasOutdatedDirectives"]
      self.HasPreProcessing:bool = obj["HasPreProcessing"]
      self.HasBaseProcessing:bool = obj["HasBaseProcessing"]
      self.HasPostProcessing:bool = obj["HasPostProcessing"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BpMethodListTableset:
   def __init__(self, obj):
      self.BpMethodList:list[Ice_Tablesets_BpMethodListRow] = obj["BpMethodList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_BpMethodRow:
   def __init__(self, obj):
      self.Source:str = obj["Source"]
      """  BPM source  """  
      self.BpMethodCode:str = obj["BpMethodCode"]
      """  BPM customization target ID  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ObjectNS:str = obj["ObjectNS"]
      """  ObjectNS  """  
      self.BusinessObject:str = obj["BusinessObject"]
      """  Referenced Business Object  """  
      self.Name:str = obj["Name"]
      """  BPM Method Name  """  
      self.Description:str = obj["Description"]
      """  BPM Method Description  """  
      self.Version:str = obj["Version"]
      """  Version  """  
      self.HasRootTransaction:bool = obj["HasRootTransaction"]
      """  Root Transaction flag  """  
      self.SignatureStatus:int = obj["SignatureStatus"]
      """  SignatureStatus  """  
      self.Disabled:bool = obj["Disabled"]
      """  BPM Method customization's enable/disable flag  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DebugMode:bool = obj["DebugMode"]
      """  DebugMode  """  
      self.DumpSources:bool = obj["DumpSources"]
      """  DumpSources  """  
      self.AdvTracing:bool = obj["AdvTracing"]
      """  AdvTracing  """  
      self.HasOutdatedDirectives:bool = obj["HasOutdatedDirectives"]
      self.HasPreProcessing:bool = obj["HasPreProcessing"]
      self.HasBaseProcessing:bool = obj["HasBaseProcessing"]
      self.HasPostProcessing:bool = obj["HasPostProcessing"]
      self.IsMDRSEnabled:bool = obj["IsMDRSEnabled"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BpMethodTableset:
   def __init__(self, obj):
      self.BpMethod:list[Ice_Tablesets_BpMethodRow] = obj["BpMethod"]
      self.BpArgument:list[Ice_Tablesets_BpArgumentRow] = obj["BpArgument"]
      self.BpDirective:list[Ice_Tablesets_BpDirectiveRow] = obj["BpDirective"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_BpWidgetRow:
   def __init__(self, obj):
      self.Name:str = obj["Name"]
      """  Widget name  """  
      self.Group:str = obj["Group"]
      """  Widget group  """  
      self.ElementType:str = obj["ElementType"]
      """  TypeName of the widget  """  
      self.Tooltip:str = obj["Tooltip"]
      """  Tooltip message, the default is the widget name  """  
      self.IconId:str = obj["IconId"]
      """  Widget icon identifier  """  
      self.DirectiveType:int = obj["DirectiveType"]
      """  Used to check if a widget applies for the directive type  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BpWidgetsTableset:
   def __init__(self, obj):
      self.BpWidget:list[Ice_Tablesets_BpWidgetRow] = obj["BpWidget"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtBpMethodTableset:
   def __init__(self, obj):
      self.BpMethod:list[Ice_Tablesets_BpMethodRow] = obj["BpMethod"]
      self.BpArgument:list[Ice_Tablesets_BpArgumentRow] = obj["BpArgument"]
      self.BpDirective:list[Ice_Tablesets_BpDirectiveRow] = obj["BpDirective"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ImportBySource_input:
   """ Required : 
   ds
   source
   """  
   def __init__(self, obj):
      self.ds      #schema had no properties on an object.
      self.source:int = obj["source"]
      pass

class ImportBySource_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BO_BpMethod_DirectiveExportImportResult] = obj["returnObj"]
      pass

class ImportMethod_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BpMethodTableset] = obj["ds"]
      pass

class ImportMethod_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Contracts_BO_BpMethod_DirectiveCompileError] = obj["returnObj"]
      """  List of outdated directive names  """  
      pass

class Import_input:
   """ Required : 
   data
   destinationGroup
   deleteExistingGroup
   """  
   def __init__(self, obj):
      self.data:str = obj["data"]
      self.destinationGroup:str = obj["destinationGroup"]
      self.deleteExistingGroup:bool = obj["deleteExistingGroup"]
      pass

class Import_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BO_BpMethod_DirectiveExportImportResult] = obj["returnObj"]
      pass

class InvalidateCaches_output:
   def __init__(self, obj):
      pass

class IsValidIdentifier_input:
   """ Required : 
   varName
   """  
   def __init__(self, obj):
      self.varName:str = obj["varName"]
      """  Variable name.  """  
      pass

class IsValidIdentifier_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if valid identifier.  """  
      pass

class PreProcessExpression_input:
   """ Required : 
   expressionDefinition
   rowVariables
   """  
   def __init__(self, obj):
      self.expressionDefinition:str = obj["expressionDefinition"]
      """  Serialized expression definition.  """  
      self.rowVariables      #schema had no properties on an object.
      """  List of row variables in the directive.  """  
      pass

class PreProcessExpression_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Preprocessed serialized expression definition.  """  
      pass

class PrepareAndSearchMethodRows_input:
   """ Required : 
   source
   whereClauseBpMethod
   whereClauseBpDirective
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.source:str = obj["source"]
      self.whereClauseBpMethod:str = obj["whereClauseBpMethod"]
      self.whereClauseBpDirective:str = obj["whereClauseBpDirective"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class PrepareAndSearchMethodRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BpMethodTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class PrepareArguments_input:
   """ Required : 
   methodRow
   """  
   def __init__(self, obj):
      self.methodRow:list[Ice_Tablesets_BpMethodRow] = obj["methodRow"]
      pass

class PrepareArguments_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BpArgumentRow] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.methodRow:list[Ice_Tablesets_BpMethodRow] = obj["methodRow"]
      pass

      """  output parameters  """  

class PrepareTriggerDefinitions_input:
   """ Required : 
   tableMask
   listMode
   """  
   def __init__(self, obj):
      self.tableMask:str = obj["tableMask"]
      """  The table mask.  """  
      self.listMode:bool = obj["listMode"]
      """  if set to `true` then table mask is treated as comma-separated list of tables.  """  
      pass

class PrepareTriggerDefinitions_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class RegisterMethodCustomization_input:
   """ Required : 
   systemCode
   serviceKind
   serviceName
   methodMask
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      """  Code of system where service defined (e.g., "ICE", "ERP")  """  
      self.serviceKind:str = obj["serviceKind"]
      """  Kind of service. The following kinds are supported: "BO", "Lib", "Proc", and "Rpt"  """  
      self.serviceName:str = obj["serviceName"]
      """  The service name.  """  
      self.methodMask:str = obj["methodMask"]
      """  The method mask.  """  
      pass

class RegisterMethodCustomization_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ShallowValidate_input:
   """ Required : 
   data
   """  
   def __init__(self, obj):
      self.data:str = obj["data"]
      pass

class ShallowValidate_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class System_Tuple_System_String_System_Boolean:
   def __init__(self, obj):
      self.Item1:str = obj["Item1"]
      self.Item2:bool = obj["Item2"]
      pass

class UpdateDirectivesByMethod_input:
   """ Required : 
   source
   methodCode
   dirInfo
   """  
   def __init__(self, obj):
      self.source:str = obj["source"]
      """  The source type (one of "BO", "DB", "DQ").  """  
      self.methodCode:str = obj["methodCode"]
      """  Name of method including system code, business object name and method name  """  
      self.dirInfo:list[Ice_Contracts_BO_BpMethod_DirectiveUpdateInfo] = obj["dirInfo"]
      pass

class UpdateDirectivesByMethod_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Contracts_BO_BpMethod_DirectiveCompileError] = obj["returnObj"]
      """  List of compilation errors if any occurs. Otherwise - empty list  """  
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtBpMethodTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtBpMethodTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BpMethodTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BpMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateCustomCode_input:
   """ Required : 
   codeSnippetWithScope
   functionDefinition
   isAsync
   """  
   def __init__(self, obj):
      self.codeSnippetWithScope:str = obj["codeSnippetWithScope"]
      """  Serialized code snippet definition.  """  
      self.functionDefinition:str = obj["functionDefinition"]
      """  Serialized function definition.  """  
      self.isAsync:bool = obj["isAsync"]
      """  Async execution.  """  
      pass

class ValidateCustomCode_output:
   def __init__(self, obj):
      self.returnObj:list[Epicor_Customization_CodeCheckResult] = obj["returnObj"]
      pass

class ValidateExpression_input:
   """ Required : 
   expressionWithScope
   functionDefinition
   """  
   def __init__(self, obj):
      self.expressionWithScope:str = obj["expressionWithScope"]
      """  Serialized expression definition.  """  
      self.functionDefinition:str = obj["functionDefinition"]
      """  Serialized function definition.  """  
      pass

class ValidateExpression_output:
   def __init__(self, obj):
      self.returnObj:list[Epicor_Customization_CodeCheckResult] = obj["returnObj"]
      pass

class ValidateKineticDirective_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BpMethodTableset] = obj["ds"]
      pass

class ValidateKineticDirective_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Array of Validation items as JSON string.
Example: [{"ElementId":"00000000-0000-0000-0000-000000000000","Element":"","Text":"Workflow validation succeeded. No issues were found","Severity":3}]  """  
      pass

class ValidateMethod_input:
   """ Required : 
   source
   businessObject
   methodName
   """  
   def __init__(self, obj):
      self.source:str = obj["source"]
      """  The source.  """  
      self.businessObject:str = obj["businessObject"]
      """  The business object.  """  
      self.methodName:str = obj["methodName"]
      """  Name of the method.  """  
      pass

class ValidateMethod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.regenMethod:bool = obj["regenMethod"]
      self.blockDirs:bool = obj["blockDirs"]
      pass

      """  output parameters  """  

class ValidateUserCode_input:
   """ Required : 
   source
   businessObject
   code
   """  
   def __init__(self, obj):
      self.source:str = obj["source"]
      """  The source.  """  
      self.businessObject:str = obj["businessObject"]
      """  The business object.  """  
      self.code:str = obj["code"]
      """  The code.  """  
      pass

class ValidateUserCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.result:int = obj["parameters"]
      self.errorMsg:str = obj["parameters"]
      self.errorRow:int = obj["parameters"]
      self.errorCol:int = obj["parameters"]
      pass

      """  output parameters  """  

