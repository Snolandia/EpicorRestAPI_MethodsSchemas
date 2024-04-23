import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.PDFFormSvc
# Description: PDF Form Service
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PDFForms(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PDFForms items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PDFForms
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.PDFFormRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/PDFForms",headers=creds) as resp:
           return await resp.json()

async def post_PDFForms(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PDFForms
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.PDFFormRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.PDFFormRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/PDFForms", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PDFForms_Company_TemplateID_FormSeq(Company, TemplateID, FormSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PDFForm item
   Description: Calls GetByID to retrieve the PDFForm item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PDFForm
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TemplateID: Desc: TemplateID   Required: True   Allow empty value : True
      :param FormSeq: Desc: FormSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.PDFFormRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/PDFForms(" + Company + "," + TemplateID + "," + FormSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PDFForms_Company_TemplateID_FormSeq(Company, TemplateID, FormSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PDFForm for the service
   Description: Calls UpdateExt to update PDFForm. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PDFForm
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TemplateID: Desc: TemplateID   Required: True   Allow empty value : True
      :param FormSeq: Desc: FormSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.PDFFormRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/PDFForms(" + Company + "," + TemplateID + "," + FormSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PDFForms_Company_TemplateID_FormSeq(Company, TemplateID, FormSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PDFForm item
   Description: Call UpdateExt to delete PDFForm item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PDFForm
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TemplateID: Desc: TemplateID   Required: True   Allow empty value : True
      :param FormSeq: Desc: FormSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/PDFForms(" + Company + "," + TemplateID + "," + FormSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PDFForms_Company_TemplateID_FormSeq_PDFFormEvents(Company, TemplateID, FormSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PDFFormEvents items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PDFFormEvents1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TemplateID: Desc: TemplateID   Required: True   Allow empty value : True
      :param FormSeq: Desc: FormSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.PDFFormEventRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/PDFForms(" + Company + "," + TemplateID + "," + FormSeq + ")/PDFFormEvents",headers=creds) as resp:
           return await resp.json()

async def get_PDFForms_Company_TemplateID_FormSeq_PDFFormEvents_SysRowID(Company, TemplateID, FormSeq, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PDFFormEvent item
   Description: Calls GetByID to retrieve the PDFFormEvent item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PDFFormEvent1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TemplateID: Desc: TemplateID   Required: True   Allow empty value : True
      :param FormSeq: Desc: FormSeq   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.PDFFormEventRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/PDFForms(" + Company + "," + TemplateID + "," + FormSeq + ")/PDFFormEvents(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PDFForms_Company_TemplateID_FormSeq_PDFFormImages(Company, TemplateID, FormSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PDFFormImages items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PDFFormImages1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TemplateID: Desc: TemplateID   Required: True   Allow empty value : True
      :param FormSeq: Desc: FormSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.PDFFormImageRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/PDFForms(" + Company + "," + TemplateID + "," + FormSeq + ")/PDFFormImages",headers=creds) as resp:
           return await resp.json()

async def get_PDFForms_Company_TemplateID_FormSeq_PDFFormImages_SysRowID(Company, TemplateID, FormSeq, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PDFFormImage item
   Description: Calls GetByID to retrieve the PDFFormImage item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PDFFormImage1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TemplateID: Desc: TemplateID   Required: True   Allow empty value : True
      :param FormSeq: Desc: FormSeq   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.PDFFormImageRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/PDFForms(" + Company + "," + TemplateID + "," + FormSeq + ")/PDFFormImages(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PDFForms_Company_TemplateID_FormSeq_PDFFormRules(Company, TemplateID, FormSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PDFFormRules items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PDFFormRules1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TemplateID: Desc: TemplateID   Required: True   Allow empty value : True
      :param FormSeq: Desc: FormSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.PDFFormRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/PDFForms(" + Company + "," + TemplateID + "," + FormSeq + ")/PDFFormRules",headers=creds) as resp:
           return await resp.json()

async def get_PDFForms_Company_TemplateID_FormSeq_PDFFormRules_SysRowID(Company, TemplateID, FormSeq, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PDFFormRule item
   Description: Calls GetByID to retrieve the PDFFormRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PDFFormRule1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TemplateID: Desc: TemplateID   Required: True   Allow empty value : True
      :param FormSeq: Desc: FormSeq   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.PDFFormRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/PDFForms(" + Company + "," + TemplateID + "," + FormSeq + ")/PDFFormRules(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PDFFormEvents(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PDFFormEvents items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PDFFormEvents
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.PDFFormEventRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/PDFFormEvents",headers=creds) as resp:
           return await resp.json()

async def post_PDFFormEvents(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PDFFormEvents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.PDFFormEventRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.PDFFormEventRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/PDFFormEvents", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PDFFormEvents_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PDFFormEvent item
   Description: Calls GetByID to retrieve the PDFFormEvent item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PDFFormEvent
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.PDFFormEventRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/PDFFormEvents(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PDFFormEvents_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PDFFormEvent for the service
   Description: Calls UpdateExt to update PDFFormEvent. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PDFFormEvent
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.PDFFormEventRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/PDFFormEvents(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PDFFormEvents_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PDFFormEvent item
   Description: Call UpdateExt to delete PDFFormEvent item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PDFFormEvent
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/PDFFormEvents(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PDFFormImages(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PDFFormImages items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PDFFormImages
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.PDFFormImageRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/PDFFormImages",headers=creds) as resp:
           return await resp.json()

async def post_PDFFormImages(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PDFFormImages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.PDFFormImageRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.PDFFormImageRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/PDFFormImages", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PDFFormImages_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PDFFormImage item
   Description: Calls GetByID to retrieve the PDFFormImage item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PDFFormImage
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.PDFFormImageRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/PDFFormImages(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PDFFormImages_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PDFFormImage for the service
   Description: Calls UpdateExt to update PDFFormImage. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PDFFormImage
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.PDFFormImageRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/PDFFormImages(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PDFFormImages_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PDFFormImage item
   Description: Call UpdateExt to delete PDFFormImage item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PDFFormImage
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/PDFFormImages(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PDFFormRules(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PDFFormRules items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PDFFormRules
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.PDFFormRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/PDFFormRules",headers=creds) as resp:
           return await resp.json()

async def post_PDFFormRules(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PDFFormRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.PDFFormRuleRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.PDFFormRuleRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/PDFFormRules", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PDFFormRules_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PDFFormRule item
   Description: Calls GetByID to retrieve the PDFFormRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PDFFormRule
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.PDFFormRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/PDFFormRules(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PDFFormRules_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PDFFormRule for the service
   Description: Calls UpdateExt to update PDFFormRule. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PDFFormRule
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.PDFFormRuleRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/PDFFormRules(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PDFFormRules_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PDFFormRule item
   Description: Call UpdateExt to delete PDFFormRule item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PDFFormRule
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/PDFFormRules(" + SysRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.PDFFormListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePDFForm, whereClausePDFFormEvent, whereClausePDFFormImage, whereClausePDFFormRule, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePDFForm=" + whereClausePDFForm
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePDFFormEvent=" + whereClausePDFFormEvent
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePDFFormImage=" + whereClausePDFFormImage
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePDFFormRule=" + whereClausePDFFormRule
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(templateID, formSeq, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
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
   params += "templateID=" + templateID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "formSeq=" + formSeq

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByRelated(schemaName, tableName, sysRowID, context, includePublished, epicorHeaders = None):
   """  
   Summary: Invoke method GetByRelated
   Description: Get the first available PDF Form by the related entity.
   OperationID: Get_GetByRelated
      :param schemaName: Desc: Schema   Required: True   Allow empty value : True
      :param tableName: Desc: Table   Required: True   Allow empty value : True
      :param sysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param context: Desc: Context   Required: True   Allow empty value : True
      :param includePublished: Desc: Whether to include published PDF Forms   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByRelated_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "schemaName=" + schemaName
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "tableName=" + tableName
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "sysRowID=" + sysRowID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "context=" + context
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "includePublished=" + includePublished

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByRelatedOrCreate(schemaName, tableName, sysRowID, context, templateID, includePublished, epicorHeaders = None):
   """  
   Summary: Invoke method GetByRelatedOrCreate
   Description: Get the first available PDF Form by the related entity or create it if not found.
   OperationID: Get_GetByRelatedOrCreate
      :param schemaName: Desc: Schema   Required: True   Allow empty value : True
      :param tableName: Desc: Table   Required: True   Allow empty value : True
      :param sysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param context: Desc: Context   Required: True   Allow empty value : True
      :param templateID: Desc: Template ID   Required: True   Allow empty value : True
      :param includePublished: Desc: Whether to include published PDF Forms   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByRelatedOrCreate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "schemaName=" + schemaName
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "tableName=" + tableName
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "sysRowID=" + sysRowID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "context=" + context
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "templateID=" + templateID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "includePublished=" + includePublished

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetImagesForPage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetImagesForPage
   Description: Get the images on the selected page
   OperationID: GetImagesForPage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetImagesForPage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetImagesForPage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PublishForm(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PublishForm
   Description: Publish the form to the entity
   OperationID: PublishForm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PublishForm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PublishForm_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExecutePageAction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExecutePageAction
   Description: Execute page action.
   OperationID: ExecutePageAction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExecutePageAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExecutePageAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPDFForm(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPDFForm
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPDFForm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPDFForm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPDFForm_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.PDFFormSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_PDFFormEventRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_PDFFormEventRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_PDFFormImageRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_PDFFormImageRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_PDFFormListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_PDFFormListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_PDFFormRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_PDFFormRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_PDFFormRuleRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_PDFFormRuleRow] = obj["value"]
      pass

class Ice_Tablesets_PDFFormEventRow:
   def __init__(self, obj):
      self.Page:int = obj["Page"]
      self.EventType:str = obj["EventType"]
      self.FieldName:str = obj["FieldName"]
      self.Context:str = obj["Context"]
      self.TemplateID:str = obj["TemplateID"]
      self.FormSeq:int = obj["FormSeq"]
      self.Company:str = obj["Company"]
      self.Sequence:int = obj["Sequence"]
      self.Trigger:str = obj["Trigger"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_PDFFormImageRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.FormSeq:int = obj["FormSeq"]
      self.ImageID:str = obj["ImageID"]
      self.ImageData:str = obj["ImageData"]
      self.Page:int = obj["Page"]
      self.Placeholder:bool = obj["Placeholder"]
      self.TemplateID:str = obj["TemplateID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_PDFFormListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.TemplateID:str = obj["TemplateID"]
      """  TemplateID  """  
      self.FormSeq:int = obj["FormSeq"]
      """  FormSeq  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_PDFFormRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.TemplateID:str = obj["TemplateID"]
      """  TemplateID  """  
      self.FormSeq:int = obj["FormSeq"]
      """  FormSeq  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  RelatedToSchemaName  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  RelatedToTableName  """  
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  RelatedToSysRowID  """  
      self.FormData:str = obj["FormData"]
      """  FormData  """  
      self.CurrentPage:int = obj["CurrentPage"]
      """  CurrentPage  """  
      self.PublishedOn:str = obj["PublishedOn"]
      """  PublishedOn  """  
      self.Context:str = obj["Context"]
      """  Context  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_PDFFormRuleRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.TemplateID:str = obj["TemplateID"]
      self.FormSeq:int = obj["FormSeq"]
      self.Page:int = obj["Page"]
      self.FieldName:str = obj["FieldName"]
      self.FieldType:str = obj["FieldType"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   templateID
   formSeq
   """  
   def __init__(self, obj):
      self.templateID:str = obj["templateID"]
      self.formSeq:int = obj["formSeq"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class ExecutePageAction_input:
   """ Required : 
   templateID
   pageNumber
   pageSequence
   formData
   """  
   def __init__(self, obj):
      self.templateID:str = obj["templateID"]
      """  Template Id  """  
      self.pageNumber:int = obj["pageNumber"]
      """  Page Number  """  
      self.pageSequence:int = obj["pageSequence"]
      """  Page Sequence  """  
      self.formData      #schema had no properties on an object.
      """  Form Data  """  
      pass

class ExecutePageAction_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  PageActionResult  """  
      pass

class GetByID_input:
   """ Required : 
   templateID
   formSeq
   """  
   def __init__(self, obj):
      self.templateID:str = obj["templateID"]
      self.formSeq:int = obj["formSeq"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_PDFFormTableset] = obj["returnObj"]
      pass

class GetByRelatedOrCreate_input:
   """ Required : 
   schemaName
   tableName
   sysRowID
   context
   templateID
   includePublished
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      """  Schema  """  
      self.tableName:str = obj["tableName"]
      """  Table  """  
      self.sysRowID:str = obj["sysRowID"]
      """  SysRowID  """  
      self.context:str = obj["context"]
      """  Context  """  
      self.templateID:str = obj["templateID"]
      """  Template ID  """  
      self.includePublished:bool = obj["includePublished"]
      """  Whether to include published PDF Forms  """  
      pass

class GetByRelatedOrCreate_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_PDFFormTableset] = obj["returnObj"]
      pass

class GetByRelated_input:
   """ Required : 
   schemaName
   tableName
   sysRowID
   context
   includePublished
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      """  Schema  """  
      self.tableName:str = obj["tableName"]
      """  Table  """  
      self.sysRowID:str = obj["sysRowID"]
      """  SysRowID  """  
      self.context:str = obj["context"]
      """  Context  """  
      self.includePublished:bool = obj["includePublished"]
      """  Whether to include published PDF Forms  """  
      pass

class GetByRelated_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_PDFFormTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_PDFFormTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_PDFFormTableset] = obj["returnObj"]
      pass

class GetImagesForPage_input:
   """ Required : 
   ds
   page
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_PDFFormTableset] = obj["ds"]
      self.page:int = obj["page"]
      pass

class GetImagesForPage_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_PDFFormTableset] = obj["ds"]
      pass

      """  output parameters  """  

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
      self.returnObj:list[Ice_Tablesets_PDFFormListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPDFForm_input:
   """ Required : 
   ds
   templateID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_PDFFormTableset] = obj["ds"]
      self.templateID:str = obj["templateID"]
      pass

class GetNewPDFForm_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_PDFFormTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePDFForm
   whereClausePDFFormEvent
   whereClausePDFFormImage
   whereClausePDFFormRule
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePDFForm:str = obj["whereClausePDFForm"]
      self.whereClausePDFFormEvent:str = obj["whereClausePDFFormEvent"]
      self.whereClausePDFFormImage:str = obj["whereClausePDFFormImage"]
      self.whereClausePDFFormRule:str = obj["whereClausePDFFormRule"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_PDFFormTableset] = obj["returnObj"]
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

class Ice_Tablesets_PDFFormEventRow:
   def __init__(self, obj):
      self.Page:int = obj["Page"]
      self.EventType:str = obj["EventType"]
      self.FieldName:str = obj["FieldName"]
      self.Context:str = obj["Context"]
      self.TemplateID:str = obj["TemplateID"]
      self.FormSeq:int = obj["FormSeq"]
      self.Company:str = obj["Company"]
      self.Sequence:int = obj["Sequence"]
      self.Trigger:str = obj["Trigger"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_PDFFormImageRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.FormSeq:int = obj["FormSeq"]
      self.ImageID:str = obj["ImageID"]
      self.ImageData:str = obj["ImageData"]
      self.Page:int = obj["Page"]
      self.Placeholder:bool = obj["Placeholder"]
      self.TemplateID:str = obj["TemplateID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_PDFFormListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.TemplateID:str = obj["TemplateID"]
      """  TemplateID  """  
      self.FormSeq:int = obj["FormSeq"]
      """  FormSeq  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_PDFFormListTableset:
   def __init__(self, obj):
      self.PDFFormList:list[Ice_Tablesets_PDFFormListRow] = obj["PDFFormList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_PDFFormRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.TemplateID:str = obj["TemplateID"]
      """  TemplateID  """  
      self.FormSeq:int = obj["FormSeq"]
      """  FormSeq  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  RelatedToSchemaName  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  RelatedToTableName  """  
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  RelatedToSysRowID  """  
      self.FormData:str = obj["FormData"]
      """  FormData  """  
      self.CurrentPage:int = obj["CurrentPage"]
      """  CurrentPage  """  
      self.PublishedOn:str = obj["PublishedOn"]
      """  PublishedOn  """  
      self.Context:str = obj["Context"]
      """  Context  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_PDFFormRuleRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.TemplateID:str = obj["TemplateID"]
      self.FormSeq:int = obj["FormSeq"]
      self.Page:int = obj["Page"]
      self.FieldName:str = obj["FieldName"]
      self.FieldType:str = obj["FieldType"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_PDFFormTableset:
   def __init__(self, obj):
      self.PDFForm:list[Ice_Tablesets_PDFFormRow] = obj["PDFForm"]
      self.PDFFormEvent:list[Ice_Tablesets_PDFFormEventRow] = obj["PDFFormEvent"]
      self.PDFFormImage:list[Ice_Tablesets_PDFFormImageRow] = obj["PDFFormImage"]
      self.PDFFormRule:list[Ice_Tablesets_PDFFormRuleRow] = obj["PDFFormRule"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtPDFFormTableset:
   def __init__(self, obj):
      self.PDFForm:list[Ice_Tablesets_PDFFormRow] = obj["PDFForm"]
      self.PDFFormEvent:list[Ice_Tablesets_PDFFormEventRow] = obj["PDFFormEvent"]
      self.PDFFormImage:list[Ice_Tablesets_PDFFormImageRow] = obj["PDFFormImage"]
      self.PDFFormRule:list[Ice_Tablesets_PDFFormRuleRow] = obj["PDFFormRule"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class PublishForm_input:
   """ Required : 
   templateID
   formSeq
   """  
   def __init__(self, obj):
      self.templateID:str = obj["templateID"]
      """  Template ID  """  
      self.formSeq:int = obj["formSeq"]
      """  Form Sequence  """  
      pass

class PublishForm_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      """  Document File Reference Number  """  
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtPDFFormTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtPDFFormTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_PDFFormTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_PDFFormTableset] = obj["ds"]
      pass

      """  output parameters  """  

