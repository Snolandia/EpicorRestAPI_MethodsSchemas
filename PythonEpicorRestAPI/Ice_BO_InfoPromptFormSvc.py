import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.InfoPromptFormSvc
# Description: 
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_InfoPromptForms(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get InfoPromptForms items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InfoPromptForms
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.IPFormRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/InfoPromptForms",headers=creds) as resp:
           return await resp.json()

async def post_InfoPromptForms(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InfoPromptForms
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.IPFormRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.IPFormRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/InfoPromptForms", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_InfoPromptForms_FormId(FormId, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InfoPromptForm item
   Description: Calls GetByID to retrieve the InfoPromptForm item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InfoPromptForm
      :param FormId: Desc: FormId   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.IPFormRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/InfoPromptForms(" + FormId + ")",headers=creds) as resp:
           return await resp.json()

async def patch_InfoPromptForms_FormId(FormId, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update InfoPromptForm for the service
   Description: Calls UpdateExt to update InfoPromptForm. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InfoPromptForm
      :param FormId: Desc: FormId   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.IPFormRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/InfoPromptForms(" + FormId + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_InfoPromptForms_FormId(FormId, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete InfoPromptForm item
   Description: Call UpdateExt to delete InfoPromptForm item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InfoPromptForm
      :param FormId: Desc: FormId   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/InfoPromptForms(" + FormId + ")",headers=creds) as resp:
           return await resp.json()

async def get_InfoPromptForms_FormId_IPFormBPActions(FormId, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get IPFormBPActions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_IPFormBPActions1
      :param FormId: Desc: FormId   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.IPFormBPActionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/InfoPromptForms(" + FormId + ")/IPFormBPActions",headers=creds) as resp:
           return await resp.json()

async def get_InfoPromptForms_FormId_IPFormBPActions_FormId_BPActionNum(FormId, BPActionNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the IPFormBPAction item
   Description: Calls GetByID to retrieve the IPFormBPAction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_IPFormBPAction1
      :param FormId: Desc: FormId   Required: True   Allow empty value : True
      :param BPActionNum: Desc: BPActionNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.IPFormBPActionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/InfoPromptForms(" + FormId + ")/IPFormBPActions(" + FormId + "," + BPActionNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_InfoPromptForms_FormId_IPFormCtrls(FormId, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get IPFormCtrls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_IPFormCtrls1
      :param FormId: Desc: FormId   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.IPFormCtrlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/InfoPromptForms(" + FormId + ")/IPFormCtrls",headers=creds) as resp:
           return await resp.json()

async def get_InfoPromptForms_FormId_IPFormCtrls_FormId_ControlId(FormId, ControlId, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the IPFormCtrl item
   Description: Calls GetByID to retrieve the IPFormCtrl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_IPFormCtrl1
      :param FormId: Desc: FormId   Required: True   Allow empty value : True
      :param ControlId: Desc: ControlId   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.IPFormCtrlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/InfoPromptForms(" + FormId + ")/IPFormCtrls(" + FormId + "," + ControlId + ")",headers=creds) as resp:
           return await resp.json()

async def get_IPFormBPActions(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get IPFormBPActions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_IPFormBPActions
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.IPFormBPActionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/IPFormBPActions",headers=creds) as resp:
           return await resp.json()

async def post_IPFormBPActions(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_IPFormBPActions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.IPFormBPActionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.IPFormBPActionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/IPFormBPActions", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_IPFormBPActions_FormId_BPActionNum(FormId, BPActionNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the IPFormBPAction item
   Description: Calls GetByID to retrieve the IPFormBPAction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_IPFormBPAction
      :param FormId: Desc: FormId   Required: True   Allow empty value : True
      :param BPActionNum: Desc: BPActionNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.IPFormBPActionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/IPFormBPActions(" + FormId + "," + BPActionNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_IPFormBPActions_FormId_BPActionNum(FormId, BPActionNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update IPFormBPAction for the service
   Description: Calls UpdateExt to update IPFormBPAction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_IPFormBPAction
      :param FormId: Desc: FormId   Required: True   Allow empty value : True
      :param BPActionNum: Desc: BPActionNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.IPFormBPActionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/IPFormBPActions(" + FormId + "," + BPActionNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_IPFormBPActions_FormId_BPActionNum(FormId, BPActionNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete IPFormBPAction item
   Description: Call UpdateExt to delete IPFormBPAction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_IPFormBPAction
      :param FormId: Desc: FormId   Required: True   Allow empty value : True
      :param BPActionNum: Desc: BPActionNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/IPFormBPActions(" + FormId + "," + BPActionNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_IPFormCtrls(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get IPFormCtrls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_IPFormCtrls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.IPFormCtrlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/IPFormCtrls",headers=creds) as resp:
           return await resp.json()

async def post_IPFormCtrls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_IPFormCtrls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.IPFormCtrlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.IPFormCtrlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/IPFormCtrls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_IPFormCtrls_FormId_ControlId(FormId, ControlId, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the IPFormCtrl item
   Description: Calls GetByID to retrieve the IPFormCtrl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_IPFormCtrl
      :param FormId: Desc: FormId   Required: True   Allow empty value : True
      :param ControlId: Desc: ControlId   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.IPFormCtrlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/IPFormCtrls(" + FormId + "," + ControlId + ")",headers=creds) as resp:
           return await resp.json()

async def patch_IPFormCtrls_FormId_ControlId(FormId, ControlId, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update IPFormCtrl for the service
   Description: Calls UpdateExt to update IPFormCtrl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_IPFormCtrl
      :param FormId: Desc: FormId   Required: True   Allow empty value : True
      :param ControlId: Desc: ControlId   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.IPFormCtrlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/IPFormCtrls(" + FormId + "," + ControlId + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_IPFormCtrls_FormId_ControlId(FormId, ControlId, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete IPFormCtrl item
   Description: Call UpdateExt to delete IPFormCtrl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_IPFormCtrl
      :param FormId: Desc: FormId   Required: True   Allow empty value : True
      :param ControlId: Desc: ControlId   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/IPFormCtrls(" + FormId + "," + ControlId + ")",headers=creds) as resp:
           return await resp.json()

async def get_IPFormCtrls_FormId_ControlId_IPFormCtrlValues(FormId, ControlId, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get IPFormCtrlValues items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_IPFormCtrlValues1
      :param FormId: Desc: FormId   Required: True   Allow empty value : True
      :param ControlId: Desc: ControlId   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.IPFormCtrlValuesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/IPFormCtrls(" + FormId + "," + ControlId + ")/IPFormCtrlValues",headers=creds) as resp:
           return await resp.json()

async def get_IPFormCtrls_FormId_ControlId_IPFormCtrlValues_FormId_ParentId_ValueSeq(FormId, ControlId, ParentId, ValueSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the IPFormCtrlValue item
   Description: Calls GetByID to retrieve the IPFormCtrlValue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_IPFormCtrlValue1
      :param FormId: Desc: FormId   Required: True   Allow empty value : True
      :param ControlId: Desc: ControlId   Required: True   Allow empty value : True
      :param ParentId: Desc: ParentId   Required: True   Allow empty value : True
      :param ValueSeq: Desc: ValueSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.IPFormCtrlValuesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/IPFormCtrls(" + FormId + "," + ControlId + ")/IPFormCtrlValues(" + FormId + "," + ParentId + "," + ValueSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_IPFormCtrlValues(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get IPFormCtrlValues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_IPFormCtrlValues
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.IPFormCtrlValuesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/IPFormCtrlValues",headers=creds) as resp:
           return await resp.json()

async def post_IPFormCtrlValues(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_IPFormCtrlValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.IPFormCtrlValuesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.IPFormCtrlValuesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/IPFormCtrlValues", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_IPFormCtrlValues_FormId_ParentId_ValueSeq(FormId, ParentId, ValueSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the IPFormCtrlValue item
   Description: Calls GetByID to retrieve the IPFormCtrlValue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_IPFormCtrlValue
      :param FormId: Desc: FormId   Required: True   Allow empty value : True
      :param ParentId: Desc: ParentId   Required: True   Allow empty value : True
      :param ValueSeq: Desc: ValueSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.IPFormCtrlValuesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/IPFormCtrlValues(" + FormId + "," + ParentId + "," + ValueSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_IPFormCtrlValues_FormId_ParentId_ValueSeq(FormId, ParentId, ValueSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update IPFormCtrlValue for the service
   Description: Calls UpdateExt to update IPFormCtrlValue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_IPFormCtrlValue
      :param FormId: Desc: FormId   Required: True   Allow empty value : True
      :param ParentId: Desc: ParentId   Required: True   Allow empty value : True
      :param ValueSeq: Desc: ValueSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.IPFormCtrlValuesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/IPFormCtrlValues(" + FormId + "," + ParentId + "," + ValueSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_IPFormCtrlValues_FormId_ParentId_ValueSeq(FormId, ParentId, ValueSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete IPFormCtrlValue item
   Description: Call UpdateExt to delete IPFormCtrlValue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_IPFormCtrlValue
      :param FormId: Desc: FormId   Required: True   Allow empty value : True
      :param ParentId: Desc: ParentId   Required: True   Allow empty value : True
      :param ValueSeq: Desc: ValueSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/IPFormCtrlValues(" + FormId + "," + ParentId + "," + ValueSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.IPFormListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseIPForm, whereClauseIPFormBPAction, whereClauseIPFormCtrl, whereClauseIPFormCtrlValues, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClauseIPForm=" + whereClauseIPForm
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseIPFormBPAction=" + whereClauseIPFormBPAction
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseIPFormCtrl=" + whereClauseIPFormCtrl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseIPFormCtrlValues=" + whereClauseIPFormCtrlValues
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(formId, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "formId=" + formId

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewIPFormCtrlRow(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewIPFormCtrlRow
   Description: Returns a new control row with completed values.
   OperationID: GetNewIPFormCtrlRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewIPFormCtrlRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewIPFormCtrlRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewIPFormCtrlValuesRow(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewIPFormCtrlValuesRow
   Description: Returns a new control values row with completed values.
   OperationID: GetNewIPFormCtrlValuesRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewIPFormCtrlValuesRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewIPFormCtrlValuesRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewIPForm(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewIPForm
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewIPForm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewIPForm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewIPForm_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewIPFormBPAction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewIPFormBPAction
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewIPFormBPAction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewIPFormBPAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewIPFormBPAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewIPFormCtrl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewIPFormCtrl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewIPFormCtrl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewIPFormCtrl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewIPFormCtrl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewIPFormCtrlValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewIPFormCtrlValues
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewIPFormCtrlValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewIPFormCtrlValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewIPFormCtrlValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.InfoPromptFormSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_IPFormBPActionRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_IPFormBPActionRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_IPFormCtrlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_IPFormCtrlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_IPFormCtrlValuesRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_IPFormCtrlValuesRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_IPFormListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_IPFormListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_IPFormRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_IPFormRow] = obj["value"]
      pass

class Ice_Tablesets_IPFormBPActionRow:
   def __init__(self, obj):
      self.FormId:str = obj["FormId"]
      """  Info Form ID  """  
      self.BPActionNum:int = obj["BPActionNum"]
      """  Info Form Action Number  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_IPFormCtrlRow:
   def __init__(self, obj):
      self.ControlId:str = obj["ControlId"]
      """  Info Form Control ID  """  
      self.FormId:str = obj["FormId"]
      """  Info Form ID  """  
      self.DataSource:str = obj["DataSource"]
      """  Data Source  """  
      self.ControlLabel:str = obj["ControlLabel"]
      """  Control Label  """  
      self.ControlFormat:str = obj["ControlFormat"]
      """  Control Format  """  
      self.Mandatory:bool = obj["Mandatory"]
      """  Mandatory flag  """  
      self.DefaultValue:str = obj["DefaultValue"]
      """  Default Value  """  
      self.DisplayOrder:int = obj["DisplayOrder"]
      """  Display order  """  
      self.ControlType:str = obj["ControlType"]
      """  Control Type  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_IPFormCtrlValuesRow:
   def __init__(self, obj):
      self.ValueMember:str = obj["ValueMember"]
      """  Value Member  """  
      self.ControlId:str = obj["ControlId"]
      """  Control ID  """  
      self.ParentId:str = obj["ParentId"]
      """  Parent ID  """  
      self.DisplayMember:str = obj["DisplayMember"]
      """  Display Member  """  
      self.ValueSeq:int = obj["ValueSeq"]
      """  Value Sequence  """  
      self.FormId:str = obj["FormId"]
      """  Info Form ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_IPFormListRow:
   def __init__(self, obj):
      self.FormId:str = obj["FormId"]
      """  Info Form ID  """  
      self.FormTitle:str = obj["FormTitle"]
      """  Info Form Title  """  
      self.FormText:str = obj["FormText"]
      """  Info Form Text  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_IPFormRow:
   def __init__(self, obj):
      self.FormId:str = obj["FormId"]
      """  Info Form ID  """  
      self.FormTitle:str = obj["FormTitle"]
      """  Info Form Title  """  
      self.FormText:str = obj["FormText"]
      """  Info Form Text  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   formId
   """  
   def __init__(self, obj):
      self.formId:str = obj["formId"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   formId
   """  
   def __init__(self, obj):
      self.formId:str = obj["formId"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_InfoPromptFormTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_InfoPromptFormTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_InfoPromptFormTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_InfoPromptFormListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewIPFormBPAction_input:
   """ Required : 
   ds
   formId
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_InfoPromptFormTableset] = obj["ds"]
      self.formId:str = obj["formId"]
      pass

class GetNewIPFormBPAction_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_InfoPromptFormTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewIPFormCtrlRow_input:
   """ Required : 
   ds
   formId
   controlType
   displayOrder
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_InfoPromptFormTableset] = obj["ds"]
      self.formId:str = obj["formId"]
      self.controlType:str = obj["controlType"]
      self.displayOrder:int = obj["displayOrder"]
      pass

class GetNewIPFormCtrlRow_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_InfoPromptFormTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewIPFormCtrlValuesRow_input:
   """ Required : 
   ds
   formId
   parentId
   sequence
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_InfoPromptFormTableset] = obj["ds"]
      self.formId:str = obj["formId"]
      self.parentId:str = obj["parentId"]
      self.sequence:int = obj["sequence"]
      pass

class GetNewIPFormCtrlValuesRow_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_InfoPromptFormTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewIPFormCtrlValues_input:
   """ Required : 
   ds
   formId
   parentId
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_InfoPromptFormTableset] = obj["ds"]
      self.formId:str = obj["formId"]
      self.parentId:str = obj["parentId"]
      pass

class GetNewIPFormCtrlValues_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_InfoPromptFormTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewIPFormCtrl_input:
   """ Required : 
   ds
   formId
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_InfoPromptFormTableset] = obj["ds"]
      self.formId:str = obj["formId"]
      pass

class GetNewIPFormCtrl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_InfoPromptFormTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewIPForm_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_InfoPromptFormTableset] = obj["ds"]
      pass

class GetNewIPForm_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_InfoPromptFormTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseIPForm
   whereClauseIPFormBPAction
   whereClauseIPFormCtrl
   whereClauseIPFormCtrlValues
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseIPForm:str = obj["whereClauseIPForm"]
      self.whereClauseIPFormBPAction:str = obj["whereClauseIPFormBPAction"]
      self.whereClauseIPFormCtrl:str = obj["whereClauseIPFormCtrl"]
      self.whereClauseIPFormCtrlValues:str = obj["whereClauseIPFormCtrlValues"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_InfoPromptFormTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

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

class Ice_Tablesets_IPFormBPActionRow:
   def __init__(self, obj):
      self.FormId:str = obj["FormId"]
      """  Info Form ID  """  
      self.BPActionNum:int = obj["BPActionNum"]
      """  Info Form Action Number  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_IPFormCtrlRow:
   def __init__(self, obj):
      self.ControlId:str = obj["ControlId"]
      """  Info Form Control ID  """  
      self.FormId:str = obj["FormId"]
      """  Info Form ID  """  
      self.DataSource:str = obj["DataSource"]
      """  Data Source  """  
      self.ControlLabel:str = obj["ControlLabel"]
      """  Control Label  """  
      self.ControlFormat:str = obj["ControlFormat"]
      """  Control Format  """  
      self.Mandatory:bool = obj["Mandatory"]
      """  Mandatory flag  """  
      self.DefaultValue:str = obj["DefaultValue"]
      """  Default Value  """  
      self.DisplayOrder:int = obj["DisplayOrder"]
      """  Display order  """  
      self.ControlType:str = obj["ControlType"]
      """  Control Type  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_IPFormCtrlValuesRow:
   def __init__(self, obj):
      self.ValueMember:str = obj["ValueMember"]
      """  Value Member  """  
      self.ControlId:str = obj["ControlId"]
      """  Control ID  """  
      self.ParentId:str = obj["ParentId"]
      """  Parent ID  """  
      self.DisplayMember:str = obj["DisplayMember"]
      """  Display Member  """  
      self.ValueSeq:int = obj["ValueSeq"]
      """  Value Sequence  """  
      self.FormId:str = obj["FormId"]
      """  Info Form ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_IPFormListRow:
   def __init__(self, obj):
      self.FormId:str = obj["FormId"]
      """  Info Form ID  """  
      self.FormTitle:str = obj["FormTitle"]
      """  Info Form Title  """  
      self.FormText:str = obj["FormText"]
      """  Info Form Text  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_IPFormRow:
   def __init__(self, obj):
      self.FormId:str = obj["FormId"]
      """  Info Form ID  """  
      self.FormTitle:str = obj["FormTitle"]
      """  Info Form Title  """  
      self.FormText:str = obj["FormText"]
      """  Info Form Text  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_InfoPromptFormListTableset:
   def __init__(self, obj):
      self.IPFormList:list[Ice_Tablesets_IPFormListRow] = obj["IPFormList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_InfoPromptFormTableset:
   def __init__(self, obj):
      self.IPForm:list[Ice_Tablesets_IPFormRow] = obj["IPForm"]
      self.IPFormBPAction:list[Ice_Tablesets_IPFormBPActionRow] = obj["IPFormBPAction"]
      self.IPFormCtrl:list[Ice_Tablesets_IPFormCtrlRow] = obj["IPFormCtrl"]
      self.IPFormCtrlValues:list[Ice_Tablesets_IPFormCtrlValuesRow] = obj["IPFormCtrlValues"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtInfoPromptFormTableset:
   def __init__(self, obj):
      self.IPForm:list[Ice_Tablesets_IPFormRow] = obj["IPForm"]
      self.IPFormBPAction:list[Ice_Tablesets_IPFormBPActionRow] = obj["IPFormBPAction"]
      self.IPFormCtrl:list[Ice_Tablesets_IPFormCtrlRow] = obj["IPFormCtrl"]
      self.IPFormCtrlValues:list[Ice_Tablesets_IPFormCtrlValuesRow] = obj["IPFormCtrlValues"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtInfoPromptFormTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtInfoPromptFormTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_InfoPromptFormTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_InfoPromptFormTableset] = obj["ds"]
      pass

      """  output parameters  """  

