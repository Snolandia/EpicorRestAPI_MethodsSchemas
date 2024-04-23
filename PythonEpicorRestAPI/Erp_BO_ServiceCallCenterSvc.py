import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ServiceCallCenterSvc
# Description: Field Service Call Center Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ServiceCallCenters(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ServiceCallCenters items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ServiceCallCenters
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSCallhdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ServiceCallCenters",headers=creds) as resp:
           return await resp.json()

async def post_ServiceCallCenters(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ServiceCallCenters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FSCallhdRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FSCallhdRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ServiceCallCenters", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ServiceCallCenters_Company_CallNum(Company, CallNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ServiceCallCenter item
   Description: Calls GetByID to retrieve the ServiceCallCenter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ServiceCallCenter
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CallNum: Desc: CallNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSCallhdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ServiceCallCenters(" + Company + "," + CallNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ServiceCallCenters_Company_CallNum(Company, CallNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ServiceCallCenter for the service
   Description: Calls UpdateExt to update ServiceCallCenter. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ServiceCallCenter
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CallNum: Desc: CallNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FSCallhdRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ServiceCallCenters(" + Company + "," + CallNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ServiceCallCenters_Company_CallNum(Company, CallNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ServiceCallCenter item
   Description: Call UpdateExt to delete ServiceCallCenter item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ServiceCallCenter
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CallNum: Desc: CallNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ServiceCallCenters(" + Company + "," + CallNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ServiceCallCenters_Company_CallNum_FSCallDts(Company, CallNum, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get FSCallDts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FSCallDts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CallNum: Desc: CallNum   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSCallDtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ServiceCallCenters(" + Company + "," + CallNum + ")/FSCallDts",headers=creds) as resp:
           return await resp.json()

async def get_ServiceCallCenters_Company_CallNum_FSCallDts_Company_CallNum_CallLine(Company, CallNum, CallLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FSCallDt item
   Description: Calls GetByID to retrieve the FSCallDt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSCallDt1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CallNum: Desc: CallNum   Required: True
      :param CallLine: Desc: CallLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSCallDtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ServiceCallCenters(" + Company + "," + CallNum + ")/FSCallDts(" + Company + "," + CallNum + "," + CallLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_ServiceCallCenters_Company_CallNum_FsTeches(Company, CallNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get FsTeches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FsTeches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CallNum: Desc: CallNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FsTechRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ServiceCallCenters(" + Company + "," + CallNum + ")/FsTeches",headers=creds) as resp:
           return await resp.json()

async def get_ServiceCallCenters_Company_CallNum_FsTeches_Company_CallNum_SeqNum(Company, CallNum, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FsTech item
   Description: Calls GetByID to retrieve the FsTech item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FsTech1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CallNum: Desc: CallNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FsTechRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ServiceCallCenters(" + Company + "," + CallNum + ")/FsTeches(" + Company + "," + CallNum + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ServiceCallCenters_Company_CallNum_FSCallhdAttches(Company, CallNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get FSCallhdAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FSCallhdAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CallNum: Desc: CallNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSCallhdAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ServiceCallCenters(" + Company + "," + CallNum + ")/FSCallhdAttches",headers=creds) as resp:
           return await resp.json()

async def get_ServiceCallCenters_Company_CallNum_FSCallhdAttches_Company_CallNum_DrawingSeq(Company, CallNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FSCallhdAttch item
   Description: Calls GetByID to retrieve the FSCallhdAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSCallhdAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CallNum: Desc: CallNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSCallhdAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/ServiceCallCenters(" + Company + "," + CallNum + ")/FSCallhdAttches(" + Company + "," + CallNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_FSCallDts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FSCallDts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FSCallDts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSCallDtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallDts",headers=creds) as resp:
           return await resp.json()

async def post_FSCallDts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FSCallDts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FSCallDtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FSCallDtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallDts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FSCallDts_Company_CallNum_CallLine(Company, CallNum, CallLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FSCallDt item
   Description: Calls GetByID to retrieve the FSCallDt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSCallDt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CallNum: Desc: CallNum   Required: True
      :param CallLine: Desc: CallLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSCallDtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallDts(" + Company + "," + CallNum + "," + CallLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FSCallDts_Company_CallNum_CallLine(Company, CallNum, CallLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FSCallDt for the service
   Description: Calls UpdateExt to update FSCallDt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FSCallDt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CallNum: Desc: CallNum   Required: True
      :param CallLine: Desc: CallLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FSCallDtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallDts(" + Company + "," + CallNum + "," + CallLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FSCallDts_Company_CallNum_CallLine(Company, CallNum, CallLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FSCallDt item
   Description: Call UpdateExt to delete FSCallDt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FSCallDt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CallNum: Desc: CallNum   Required: True
      :param CallLine: Desc: CallLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallDts(" + Company + "," + CallNum + "," + CallLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_FSCallDts_Company_CallNum_CallLine_FSCallDtAttches(Company, CallNum, CallLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get FSCallDtAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FSCallDtAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CallNum: Desc: CallNum   Required: True
      :param CallLine: Desc: CallLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSCallDtAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallDts(" + Company + "," + CallNum + "," + CallLine + ")/FSCallDtAttches",headers=creds) as resp:
           return await resp.json()

async def get_FSCallDts_Company_CallNum_CallLine_FSCallDtAttches_Company_CallNum_CallLine_DrawingSeq(Company, CallNum, CallLine, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FSCallDtAttch item
   Description: Calls GetByID to retrieve the FSCallDtAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSCallDtAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CallNum: Desc: CallNum   Required: True
      :param CallLine: Desc: CallLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSCallDtAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallDts(" + Company + "," + CallNum + "," + CallLine + ")/FSCallDtAttches(" + Company + "," + CallNum + "," + CallLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_FSCallDtAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FSCallDtAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FSCallDtAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSCallDtAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallDtAttches",headers=creds) as resp:
           return await resp.json()

async def post_FSCallDtAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FSCallDtAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FSCallDtAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FSCallDtAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallDtAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FSCallDtAttches_Company_CallNum_CallLine_DrawingSeq(Company, CallNum, CallLine, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FSCallDtAttch item
   Description: Calls GetByID to retrieve the FSCallDtAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSCallDtAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CallNum: Desc: CallNum   Required: True
      :param CallLine: Desc: CallLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSCallDtAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallDtAttches(" + Company + "," + CallNum + "," + CallLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FSCallDtAttches_Company_CallNum_CallLine_DrawingSeq(Company, CallNum, CallLine, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FSCallDtAttch for the service
   Description: Calls UpdateExt to update FSCallDtAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FSCallDtAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CallNum: Desc: CallNum   Required: True
      :param CallLine: Desc: CallLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FSCallDtAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallDtAttches(" + Company + "," + CallNum + "," + CallLine + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FSCallDtAttches_Company_CallNum_CallLine_DrawingSeq(Company, CallNum, CallLine, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FSCallDtAttch item
   Description: Call UpdateExt to delete FSCallDtAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FSCallDtAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CallNum: Desc: CallNum   Required: True
      :param CallLine: Desc: CallLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallDtAttches(" + Company + "," + CallNum + "," + CallLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_FsTeches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FsTeches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FsTeches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FsTechRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FsTeches",headers=creds) as resp:
           return await resp.json()

async def post_FsTeches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FsTeches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FsTechRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FsTechRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FsTeches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FsTeches_Company_CallNum_SeqNum(Company, CallNum, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FsTech item
   Description: Calls GetByID to retrieve the FsTech item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FsTech
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CallNum: Desc: CallNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FsTechRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FsTeches(" + Company + "," + CallNum + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FsTeches_Company_CallNum_SeqNum(Company, CallNum, SeqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FsTech for the service
   Description: Calls UpdateExt to update FsTech. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FsTech
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CallNum: Desc: CallNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FsTechRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FsTeches(" + Company + "," + CallNum + "," + SeqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FsTeches_Company_CallNum_SeqNum(Company, CallNum, SeqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FsTech item
   Description: Call UpdateExt to delete FsTech item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FsTech
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CallNum: Desc: CallNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FsTeches(" + Company + "," + CallNum + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_FSCallhdAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FSCallhdAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FSCallhdAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSCallhdAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallhdAttches",headers=creds) as resp:
           return await resp.json()

async def post_FSCallhdAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FSCallhdAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FSCallhdAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FSCallhdAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallhdAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FSCallhdAttches_Company_CallNum_DrawingSeq(Company, CallNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FSCallhdAttch item
   Description: Calls GetByID to retrieve the FSCallhdAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSCallhdAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CallNum: Desc: CallNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSCallhdAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallhdAttches(" + Company + "," + CallNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FSCallhdAttches_Company_CallNum_DrawingSeq(Company, CallNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FSCallhdAttch for the service
   Description: Calls UpdateExt to update FSCallhdAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FSCallhdAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CallNum: Desc: CallNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FSCallhdAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallhdAttches(" + Company + "," + CallNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FSCallhdAttches_Company_CallNum_DrawingSeq(Company, CallNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FSCallhdAttch item
   Description: Call UpdateExt to delete FSCallhdAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FSCallhdAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CallNum: Desc: CallNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/FSCallhdAttches(" + Company + "," + CallNum + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSCallhdListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseFSCallhd, whereClauseFSCallhdAttch, whereClauseFSCallDt, whereClauseFSCallDtAttch, whereClauseFsTech, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClauseFSCallhd=" + whereClauseFSCallhd
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFSCallhdAttch=" + whereClauseFSCallhdAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFSCallDt=" + whereClauseFSCallDt
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFSCallDtAttch=" + whereClauseFSCallDtAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFsTech=" + whereClauseFsTech
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(callNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "callNum=" + callNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ExpireDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExpireDate
   Description: Expire Date
   OperationID: ExpireDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExpireDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExpireDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ActivateServiceCall(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ActivateServiceCall
   Description: This method activates the Service Call.
   OperationID: ActivateServiceCall
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ActivateServiceCall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ActivateServiceCall_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AssignTechnician(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AssignTechnician
   Description: This method assigns a Service Technician to a service call.
   OperationID: AssignTechnician
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignTechnician_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignTechnician_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDtlContractLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDtlContractLine
   Description: Update Service Call Line Contract information when the Contract Line Number field changes.
   OperationID: ChangeDtlContractLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlContractLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlContractLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDtlContractNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDtlContractNum
   Description: Update Service Call Line Contract information when the Contract Number field changes.
   OperationID: ChangeDtlContractNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlContractNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlContractNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDtlDropShipPackLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDtlDropShipPackLine
   Description: Update Service Call Line Warranty information when the Drop Shipment PackLine Number field changes.
   OperationID: ChangeDtlDropShipPackLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlDropShipPackLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlDropShipPackLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDtlDropShipPackSlip(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDtlDropShipPackSlip
   Description: Update Service Call Line Warranty information when the Drop Shipment PackSlip field changes.
   OperationID: ChangeDtlDropShipPackSlip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlDropShipPackSlip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlDropShipPackSlip_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDtlPackLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDtlPackLine
   Description: Update Service Call Line Warranty information when the Pack Line Number field changes.
   OperationID: ChangeDtlPackLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlPackLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlPackLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDtlPackNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDtlPackNum
   Description: Update Service Call Line Warranty information when the Pack ID field changes.
   OperationID: ChangeDtlPackNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlPackNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlPackNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDtlPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDtlPartNum
   Description: Update Service Call Line information when the Part Number field changes.
   OperationID: ChangeDtlPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDtlRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDtlRevisionNum
   Description: Update Service Call Line information when the Revision Number field changes.
   OperationID: ChangeDtlRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDtlSerialNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDtlSerialNum
   Description: Update Service Call Line Serial Number/Contract information when the Serial Number field changes.
   OperationID: ChangeDtlSerialNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlSerialNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlSerialNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDtlXPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDtlXPartNum
   Description: Update Service Call Line information when the Customer Part Number field changes.
   OperationID: ChangeDtlXPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlXPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlXPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSCallDtProjectID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSCallDtProjectID
   Description: Method to call when changing the project id on the service call detail record.
Validates the id and updates FSCallDt with values from the project.
   OperationID: ChangeFSCallDtProjectID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSCallDtProjectID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSCallDtProjectID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeHdrBillToContact(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeHdrBillToContact
   Description: This method updates the related Customer Contact information when the Customer
Bill To Contact field (FSCallHd.PrcConNum) changes.
   OperationID: ChangeHdrBillToContact
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHdrBillToContact_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHdrBillToContact_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeHdrCallCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeHdrCallCode
   Description: This method gets the default Tax Category and Call Comment when the Service
Call Type field (FSCallHd.CallCode) changes.
   OperationID: ChangeHdrCallCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHdrCallCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHdrCallCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeHdrCurrencyCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeHdrCurrencyCode
   Description: This method gets the appropriate exchange rate for the new currency.  Call this
method when the field FSCallHd.CurrencyCode changes.
   OperationID: ChangeHdrCurrencyCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHdrCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHdrCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeHdrCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeHdrCustID
   Description: This method updates the related Customer and ShipTo information when the Customer ID
field (FSCallHd.CustNumCustID) changes.
   OperationID: ChangeHdrCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHdrCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHdrCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeHdrRequestTime(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeHdrRequestTime
   Description: Validates the entered RequestTime.
   OperationID: ChangeHdrRequestTime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHdrRequestTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHdrRequestTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeHdrSchedTime(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeHdrSchedTime
   Description: This method validates the entered Scheduled Time.  Call this method when the
field FSCallHd.DispSchedTime changes.
   OperationID: ChangeHdrSchedTime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHdrSchedTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHdrSchedTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeHdrShipToContact(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeHdrShipToContact
   Description: This method updates the related Customer Ship To Contact information when the Customer
Ship To Contact field (FSCallHd.ShpConNum) changes.
   OperationID: ChangeHdrShipToContact
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHdrShipToContact_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHdrShipToContact_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeHdrShipToCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeHdrShipToCustID
   Description: This method updates the ShipTo information when the ShipToCustID
field (Link) changes.
   OperationID: ChangeHdrShipToCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHdrShipToCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHdrShipToCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeHdrShipToNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeHdrShipToNum
   Description: This method updates the related ShipTo information when the Customer ShipTo Number
field (FSCallHd.ShipToNum) changes.
   OperationID: ChangeHdrShipToNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHdrShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHdrShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeHdrUseOTS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeHdrUseOTS
   Description: Method to call when changing the UseOTS field.
Refreshes the address list and contact info
   OperationID: ChangeHdrUseOTS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHdrUseOTS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHdrUseOTS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeHdrHDCaseNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeHdrHDCaseNum
   Description: This method validates the proposed Case Number.
   OperationID: ChangeHdrHDCaseNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHdrHDCaseNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHdrHDCaseNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckDtlSerialNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckDtlSerialNum
   Description: Check the serial number field and return messages about the serial number to
the user.  The method will check the following:
The serial number exists
The customer and ship to matches
The part number on the line matches the serial part number
The contract number and line matches (if applicable)
The pack id matches (if appicable)
If any of these conditions are met where the data in the service contract doesn
not match the data for the serial number, the user is prompted with this information
and asked if they would like to continue with the save.
   OperationID: CheckDtlSerialNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDtlSerialNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDtlSerialNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPrePartInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPrePartInfo
   Description: This method checks to see if there are any questions or issues with the part entered
and returns a message, a part number and if any substitutes exist.  Call this method
first before calling the ChangeDtlPartNum method when the field FSCallDt.PartNum changes.
   OperationID: CheckPrePartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPrePartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPrePartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckRateGrpCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckRateGrpCode
   Description: Update Service Call information when the currency is changed.
   OperationID: CheckRateGrpCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckRateGrpCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRateGrpCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CloseServiceCall(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CloseServiceCall
   Description: This method closes the Service Call.  Run this method after calling PreCloseServiceCall.
   OperationID: CloseServiceCall
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseServiceCall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseServiceCall_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateServiceCallJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateServiceCallJob
   Description: This method creates the Service Call Job for the service call line.  A warning message
is returned by this method if the service call plant and the current plant is not the
same.  Do not call the JobEntry object if the opMessage is not blank.
   OperationID: CreateServiceCallJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateServiceCallJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateServiceCallJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetXPartByPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetXPartByPartNum
   Description: This method gets the first CustXPart found by using customer number and part number to find it.
   OperationID: GetXPartByPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetXPartByPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetXPartByPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FindPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FindPart
   Description: FindPart
   OperationID: FindPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartFromRowID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartFromRowID
   Description: GetPartFromRowID.
   OperationID: GetPartFromRowID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartFromRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartFromRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: Method to call to get a Code Description list.
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFSCallhdReadyForInvoice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFSCallhdReadyForInvoice
   Description: Returns list of FSCallHd ready to be invoiced.
The standard GetList will not work anymore because need to only return rows where Job is open
   OperationID: GetFSCallhdReadyForInvoice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFSCallhdReadyForInvoice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFSCallhdReadyForInvoice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListRemoveInvoiced(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListRemoveInvoiced
   Description: Returns a list of FSCallhd rows that satisfy the where clause and remove invoiced detail lines
   OperationID: GetListRemoveInvoiced
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListRemoveInvoiced_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListRemoveInvoiced_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFSCallHd1(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFSCallHd1
   Description: This method is to be used in place of GetNewFSCallHd.  This method asks for
customer number and shipto number to default the fields based on the customer/shipto.
   OperationID: GetNewFSCallHd1
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFSCallHd1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSCallHd1_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartXRefInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartXRefInfo
   Description: This method defaults PartAdvisor fields when the PartNum field changes
   OperationID: GetPartXRefInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartXRefInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartXRefInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsContactTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsContactTracker
   Description: Calls the normal GetRows method and then constructs a custom data set combining Hed/Dtl fields for the customer tracker.
   OperationID: GetRowsContactTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsContactTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsContactTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCustomerTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustomerTracker
   Description: Calls the normal GetRows method and then constructs a custom data set combining Hed/Dtl fields for the customer tracker.
   OperationID: GetRowsCustomerTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustomerTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomerTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreCloseServiceCall(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreCloseServiceCall
   Description: Checks to see if the service call can be closed and gives a warning message
to let the user decide to continue closing or not.  This method should be called
prior to calling the CloseServiceCall method which does the actual closing logic.
If a warning message returns with this method and the user chooses to continue
or NO warning message then call CloseServiceCall method else cancel close request.
   OperationID: PreCloseServiceCall
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreCloseServiceCall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreCloseServiceCall_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReopenServiceCall(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReopenServiceCall
   Description: This method reopens the Service Call.
   OperationID: ReopenServiceCall
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReopenServiceCall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReopenServiceCall_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidServiceCall(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidServiceCall
   Description: This method voids the Service Call.
   OperationID: VoidServiceCall
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidServiceCall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidServiceCall_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeIssueTopics(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeIssueTopics
   Description: This method should be invoked when the IssueTopics changes.
Validates and sets the individual IssueTopic fields.
   OperationID: ChangeIssueTopics
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeIssueTopics_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeIssueTopics_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeResTopics(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeResTopics
   Description: This method should be invoked when the ResTopics changes.
Validates and sets the individual ResTopic fields.
   OperationID: ChangeResTopics
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeResTopics_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeResTopics_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeBTCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeBTCustID
   Description: This method updates the Bill To customer info.
   OperationID: ChangeBTCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBTCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBTCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateOTSTaxID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateOTSTaxID
   Description: ValidateOTSTaxID
   OperationID: ValidateOTSTaxID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateOTSTaxID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateOTSTaxID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFSCallhd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFSCallhd
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFSCallhd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFSCallhd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSCallhd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFSCallhdAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFSCallhdAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFSCallhdAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFSCallhdAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSCallhdAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFSCallDt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFSCallDt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFSCallDt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFSCallDt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSCallDt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFSCallDtAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFSCallDtAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFSCallDtAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFSCallDtAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSCallDtAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFsTech(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFsTech
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFsTech
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFsTech_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFsTech_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceCallCenterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallDtAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FSCallDtAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallDtRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FSCallDtRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallhdAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FSCallhdAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallhdListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FSCallhdListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallhdRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FSCallhdRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FsTechRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FsTechRow] = obj["value"]
      pass

class Erp_Tablesets_FSCallDtAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CallNum:int = obj["CallNum"]
      self.CallLine:int = obj["CallLine"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSCallDtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CallNum:int = obj["CallNum"]
      """  When creating a new Service Call ,the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  """  
      self.CallLine:int = obj["CallLine"]
      """  This field along with Company and CallNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last FSCalPrt record for the Call and the adding 1 to it.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial number of the part being repaired.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  """  
      self.CallQty:int = obj["CallQty"]
      """  TotalCall Quantity for the line item.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this Service call is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  The packing slip line that holds the warranty information for this service call  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number if this item is under a contract  """  
      self.ContractLine:int = obj["ContractLine"]
      """  This is the contract line the relates to the item on the service call.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Contract  """  
      self.CallComment:str = obj["CallComment"]
      """  Contains comments about the Item in need of service. These will be printed on the ServiceCall.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the repaired item. These will copied into the Invoice detail file as defaults.  """  
      self.ProbReasonCode:str = obj["ProbReasonCode"]
      """  Problem reason code from the reason master table. type problem.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the xasyst.CallProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  """  
      self.MatCovered:bool = obj["MatCovered"]
      """  Are Material cost covered  """  
      self.LabCovered:bool = obj["LabCovered"]
      """  Is Labor Cost Covered  """  
      self.MiscCovered:bool = obj["MiscCovered"]
      """  Are misc. Costs Covered  """  
      self.TotLabor:int = obj["TotLabor"]
      """  total Labor Amount.  """  
      self.DocTotLabor:int = obj["DocTotLabor"]
      """  total Labor Amount. In customers currency  """  
      self.TotBillLabor:int = obj["TotBillLabor"]
      """  total Billable Labor Amount.  """  
      self.DocTotBillLabor:int = obj["DocTotBillLabor"]
      """  total Billable Labor Amount. In Customers currency.  """  
      self.TotMaterial:int = obj["TotMaterial"]
      """  total Material Amount.  """  
      self.DocTotMaterial:int = obj["DocTotMaterial"]
      """  total Material Amount. In Customers currency  """  
      self.TotBillMaterial:int = obj["TotBillMaterial"]
      """  total Billable Material Amount.  """  
      self.DocTotBillMaterial:int = obj["DocTotBillMaterial"]
      """  total Billable Material Amount. In Customers Currency.  """  
      self.TotMisc:int = obj["TotMisc"]
      """  total Misc. Amount.  """  
      self.DocTotMisc:int = obj["DocTotMisc"]
      """  total Misc. Amount. In customers currency.  """  
      self.TotBillableMisc:int = obj["TotBillableMisc"]
      """  total Billable Misc. Amount.  """  
      self.DocTotBillableMisc:int = obj["DocTotBillableMisc"]
      """  total Billable Misc. Amount. In customer's currency.  """  
      self.TotMaterialCost:int = obj["TotMaterialCost"]
      """  total Material Cost.  """  
      self.TotMiscCost:int = obj["TotMiscCost"]
      """  total Misc. Cost.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record that this FSCallDt record. Can be blank.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  Associates the Call Line record back its linked JobHead record.  Not directly maintainable.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.TotSubCont:int = obj["TotSubCont"]
      """  Total Subcontract Amount.  """  
      self.DocTotSubCont:int = obj["DocTotSubCont"]
      """  total Subcontract Amount. In customers currency  """  
      self.TotBillSubCont:int = obj["TotBillSubCont"]
      """  total Billable Subcontract Amount.  """  
      self.DocTotBillSubCont:int = obj["DocTotBillSubCont"]
      """  total Billable Subcontract Amount. In Customers currency.  """  
      self.TotEstLabor:int = obj["TotEstLabor"]
      """  total Estimated Labor Amount.  """  
      self.DocTotEstLabor:int = obj["DocTotEstLabor"]
      """  total estimated Labor Amount. In customers currency  """  
      self.TotEstMaterial:int = obj["TotEstMaterial"]
      """  total Estimated Material Amount.  """  
      self.DocTotEstMaterial:int = obj["DocTotEstMaterial"]
      """  total Estimated Material Amount. In Customers currency  """  
      self.TotEstMisc:int = obj["TotEstMisc"]
      """  total Estimated Misc. Amount.  Future Use.  """  
      self.DocTotEstMisc:int = obj["DocTotEstMisc"]
      """  total Est. Misc. Amount. In customers currency. Future use  """  
      self.TotEstSubCont:int = obj["TotEstSubCont"]
      """  Total estimated Subcontract Amount.  """  
      self.DocTotEstSubCont:int = obj["DocTotEstSubCont"]
      """  total Estimated Subcontract Amount. In customers currency  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.Rpt1TotBillableMisc:int = obj["Rpt1TotBillableMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotBillableMisc:int = obj["Rpt2TotBillableMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotBillableMisc:int = obj["Rpt3TotBillableMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotBillLabor:int = obj["Rpt1TotBillLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotBillLabor:int = obj["Rpt2TotBillLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotBillLabor:int = obj["Rpt3TotBillLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotBillMaterial:int = obj["Rpt1TotBillMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotBillMaterial:int = obj["Rpt2TotBillMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotBillMaterial:int = obj["Rpt3TotBillMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotBillSubCont:int = obj["Rpt1TotBillSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotBillSubCont:int = obj["Rpt2TotBillSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotBillSubCont:int = obj["Rpt3TotBillSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotEstLabor:int = obj["Rpt1TotEstLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotEstLabor:int = obj["Rpt2TotEstLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotEstLabor:int = obj["Rpt3TotEstLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotEstMaterial:int = obj["Rpt1TotEstMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotEstMaterial:int = obj["Rpt2TotEstMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotEstMaterial:int = obj["Rpt3TotEstMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotEstMisc:int = obj["Rpt1TotEstMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotEstMisc:int = obj["Rpt2TotEstMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotEstMisc:int = obj["Rpt3TotEstMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotEstSubCont:int = obj["Rpt1TotEstSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotEstSubCont:int = obj["Rpt2TotEstSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotEstSubCont:int = obj["Rpt3TotEstSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotLabor:int = obj["Rpt1TotLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotLabor:int = obj["Rpt2TotLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotLabor:int = obj["Rpt3TotLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotMaterial:int = obj["Rpt1TotMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotMaterial:int = obj["Rpt2TotMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotMaterial:int = obj["Rpt3TotMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotMisc:int = obj["Rpt1TotMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotMisc:int = obj["Rpt2TotMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotMisc:int = obj["Rpt3TotMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotSubCont:int = obj["Rpt1TotSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotSubCont:int = obj["Rpt2TotSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotSubCont:int = obj["Rpt3TotSubCont"]
      """  Reporting currency value of this field  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  The drop shipment packing slip number that this Service call is linked with  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  The drop shipment packing slip line that holds the warranty information for this service call  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier number of the drop shipment and part of the primary key of a drop shipment line.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The supplier purchase point id of the drop shipment and part of the primary key of a drop shipment line.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.POLine:str = obj["POLine"]
      """  POLine  """  
      self.IssueTopicID1:str = obj["IssueTopicID1"]
      """  IssueTopicID1  """  
      self.IssueTopicID2:str = obj["IssueTopicID2"]
      """  IssueTopicID2  """  
      self.IssueTopicID3:str = obj["IssueTopicID3"]
      """  IssueTopicID3  """  
      self.IssueTopicID4:str = obj["IssueTopicID4"]
      """  IssueTopicID4  """  
      self.IssueTopicID5:str = obj["IssueTopicID5"]
      """  IssueTopicID5  """  
      self.IssueTopicID6:str = obj["IssueTopicID6"]
      """  IssueTopicID6  """  
      self.IssueTopicID7:str = obj["IssueTopicID7"]
      """  IssueTopicID7  """  
      self.IssueTopicID8:str = obj["IssueTopicID8"]
      """  IssueTopicID8  """  
      self.IssueTopicID9:str = obj["IssueTopicID9"]
      """  IssueTopicID9  """  
      self.IssueTopicID10:str = obj["IssueTopicID10"]
      """  IssueTopicID10  """  
      self.IssueTopics:str = obj["IssueTopics"]
      """  IssueTopics  """  
      self.ResTopicID1:str = obj["ResTopicID1"]
      """  ResTopicID1  """  
      self.ResTopicID2:str = obj["ResTopicID2"]
      """  ResTopicID2  """  
      self.ResTopicID3:str = obj["ResTopicID3"]
      """  ResTopicID3  """  
      self.ResTopicID4:str = obj["ResTopicID4"]
      """  ResTopicID4  """  
      self.ResTopicID5:str = obj["ResTopicID5"]
      """  ResTopicID5  """  
      self.ResTopicID6:str = obj["ResTopicID6"]
      """  ResTopicID6  """  
      self.ResTopicID7:str = obj["ResTopicID7"]
      """  ResTopicID7  """  
      self.ResTopicID8:str = obj["ResTopicID8"]
      """  ResTopicID8  """  
      self.ResTopicID9:str = obj["ResTopicID9"]
      """  ResTopicID9  """  
      self.ResTopicID10:str = obj["ResTopicID10"]
      """  ResTopicID10  """  
      self.ResTopics:str = obj["ResTopics"]
      """  ResTopics  """  
      self.PartDescription:str = obj["PartDescription"]
      """  PartDescription  """  
      self.CommentText:str = obj["CommentText"]
      """  CommentText  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Indicates the invoice processing has been done for this call line.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates that the call line can be invoiced.  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol of the "BASE" currency  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DisplayContractType:str = obj["DisplayContractType"]
      self.DocCurrSymbol:str = obj["DocCurrSymbol"]
      """  Currency.CurrSymbol of the customer's currency  """  
      self.DocTotLineBillCall:int = obj["DocTotLineBillCall"]
      """  Total Billable Call Amount for the line in customer's currency  """  
      self.DocTotLineCall:int = obj["DocTotLineCall"]
      """  Total Actual Call Amount for the line in customer's currency  """  
      self.DocTotLineEstCall:int = obj["DocTotLineEstCall"]
      """  Total Estimated Call AMount for the line in customer's currency  """  
      self.EnableContract:bool = obj["EnableContract"]
      """  Indicates if Contract entry should be enabled.  """  
      self.EnableWarranty:bool = obj["EnableWarranty"]
      """  Indicates if Warranty entry should be enabled.  """  
      self.IUMDesc:str = obj["IUMDesc"]
      """  Unit of Measure Description  """  
      self.ProbReasonDesc:str = obj["ProbReasonDesc"]
      """  Reson Code Description  """  
      self.Rpt1TotLineBillCall:int = obj["Rpt1TotLineBillCall"]
      self.Rpt1TotLineCall:int = obj["Rpt1TotLineCall"]
      self.Rpt1TotLineEstCall:int = obj["Rpt1TotLineEstCall"]
      self.Rpt2TotLineBillCall:int = obj["Rpt2TotLineBillCall"]
      self.Rpt2TotLineCall:int = obj["Rpt2TotLineCall"]
      self.Rpt2TotLineEstCall:int = obj["Rpt2TotLineEstCall"]
      self.Rpt3TotLineBillCall:int = obj["Rpt3TotLineBillCall"]
      self.Rpt3TotLineCall:int = obj["Rpt3TotLineCall"]
      self.Rpt3TotLineEstCall:int = obj["Rpt3TotLineEstCall"]
      self.TotLineBillCall:int = obj["TotLineBillCall"]
      """  Total Billable Call Amount for the line  """  
      self.TotLineCall:int = obj["TotLineCall"]
      """  Total Actual Call Amount for the line  """  
      self.TotLineEstCall:int = obj["TotLineEstCall"]
      """  Total Estimated Call Amount for the line  """  
      self.JobClosed:bool = obj["JobClosed"]
      self.BitFlag:int = obj["BitFlag"]
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      self.ContractLineLineDesc:str = obj["ContractLineLineDesc"]
      self.DropShipDtlLineDesc:str = obj["DropShipDtlLineDesc"]
      self.IssueTopicID1Description:str = obj["IssueTopicID1Description"]
      self.IssueTopicID10Description:str = obj["IssueTopicID10Description"]
      self.IssueTopicID2Description:str = obj["IssueTopicID2Description"]
      self.IssueTopicID3Description:str = obj["IssueTopicID3Description"]
      self.IssueTopicID4Description:str = obj["IssueTopicID4Description"]
      self.IssueTopicID5Description:str = obj["IssueTopicID5Description"]
      self.IssueTopicID6Description:str = obj["IssueTopicID6Description"]
      self.IssueTopicID7Description:str = obj["IssueTopicID7Description"]
      self.IssueTopicID8Description:str = obj["IssueTopicID8Description"]
      self.IssueTopicID9Description:str = obj["IssueTopicID9Description"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.PackLineLineDesc:str = obj["PackLineLineDesc"]
      self.PackNumShipStatus:str = obj["PackNumShipStatus"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.ResTopicID1Description:str = obj["ResTopicID1Description"]
      self.ResTopicID10Description:str = obj["ResTopicID10Description"]
      self.ResTopicID2Description:str = obj["ResTopicID2Description"]
      self.ResTopicID3Description:str = obj["ResTopicID3Description"]
      self.ResTopicID4Description:str = obj["ResTopicID4Description"]
      self.ResTopicID5Description:str = obj["ResTopicID5Description"]
      self.ResTopicID6Description:str = obj["ResTopicID6Description"]
      self.ResTopicID7Description:str = obj["ResTopicID7Description"]
      self.ResTopicID8Description:str = obj["ResTopicID8Description"]
      self.ResTopicID9Description:str = obj["ResTopicID9Description"]
      self.WarrantyCodeWarrDescription:str = obj["WarrantyCodeWarrDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSCallhdAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CallNum:int = obj["CallNum"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSCallhdListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CallNum:int = obj["CallNum"]
      """  When creating a new Service Call the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the Service Call is for.  This must be valid in the Customer table.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Customer Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used  for the Service Call. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Establishes the Shipping Contact to be used.  In this case the contact at the location where the item the service call is covering are. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  """  
      self.EntryDate:str = obj["EntryDate"]
      """  defaults to TODAY  """  
      self.EntryTime:int = obj["EntryTime"]
      """  Time in second past midnight  """  
      self.RequestDate:str = obj["RequestDate"]
      """  The date that the service is requested for.  """  
      self.RequestTime:int = obj["RequestTime"]
      """  Time in second past midnight  """  
      self.SchedDate:str = obj["SchedDate"]
      """  The date that the service is scheduled for.  """  
      self.SchedTime:int = obj["SchedTime"]
      """  Time in second past midnight  """  
      self.ActualDate:str = obj["ActualDate"]
      """  The date that the service was performed on.  """  
      self.ActualTime:int = obj["ActualTime"]
      """  Time in second past midnight  """  
      self.CallComment:str = obj["CallComment"]
      """  Contains comments about the overall Call. These will be printed on the Service Call.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Contains comments about the overall Call. These will be printed on the Service Call invoice.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this Call.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.OpenCall:bool = obj["OpenCall"]
      """  Indicate that the call is open.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates that the call is closed and can be invoiced.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Indicated the invoice processing has been done for this call.  """  
      self.VoidCall:bool = obj["VoidCall"]
      """  No information can be entered when this flag is set. It won't be invoiced, labor and materials cannot be entered.  """  
      self.CallPriority:str = obj["CallPriority"]
      """  Can have 3 values High, normal and, Low  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as one of the selection parameters on the Service call entry edit reports. The intent is for users to be able to select Contract that they have entered for hard copy edit.
On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  """  
      self.CallCode:str = obj["CallCode"]
      """  A unique code that identifies the type of service call  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record.  """  
      self.LaborComplete:bool = obj["LaborComplete"]
      """   Set from labor entry.  Indicates that all labor has been entered for this call.  if this flag and the Material complete flag are set then the
opencall field will be set to FALSE and the READY TO INVOICE flag will be set o TRUE.  """  
      self.MaterialComplete:bool = obj["MaterialComplete"]
      """  Set from Issue materials.  Indicates that all material have been issued for this call.  if this flag and the Labor complete flag are set then the opencall field will be set to FALSE and the READY TO INVOICE flag will be set to TRUE.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Duration:int = obj["Duration"]
      """  The estimated duration of the service call in days.  """  
      self.CLCallNum:str = obj["CLCallNum"]
      """  The Clientele call number that is related to this call.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this service call.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping country number  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustConName:str = obj["CustConName"]
      """  Customer Contact Name  """  
      self.CustPhoneNum:str = obj["CustPhoneNum"]
      """  Customer Phone Number  """  
      self.CustFaxNum:str = obj["CustFaxNum"]
      """  Customer Fax Number  """  
      self.ShipConName:str = obj["ShipConName"]
      """  ShipTo Contact Name  """  
      self.ShipPhoneNum:str = obj["ShipPhoneNum"]
      """  ShipTo Phone Number  """  
      self.ShipFaxNum:str = obj["ShipFaxNum"]
      """  ShipTo Fax Number  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currency Switch  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for currency "BASE"  """  
      self.XRateLabel:str = obj["XRateLabel"]
      """  Exchange Rate Label  """  
      self.TotEstMaterial:int = obj["TotEstMaterial"]
      """  Total Estimated Material Amount  """  
      self.DocTotEstMaterial:int = obj["DocTotEstMaterial"]
      """  Total Estimated Mateiral Amount in customer's currency  """  
      self.TotEstSubContract:int = obj["TotEstSubContract"]
      """  Total Estimated Subcontract Amount  """  
      self.DocTotEstSubcontract:int = obj["DocTotEstSubcontract"]
      """  Total Estimated Subcontract Amount in customer's currency  """  
      self.TotEstMisc:int = obj["TotEstMisc"]
      """  Total Estimated Miscellaneous Amount  """  
      self.DocTotEstMisc:int = obj["DocTotEstMisc"]
      """  Total Estimated Miscellaneous Amount in customer's currency  """  
      self.TotEstCall:int = obj["TotEstCall"]
      """  Total Estimated Call Amount  """  
      self.DocTotEstCall:int = obj["DocTotEstCall"]
      """  Total Estimated Call Amount in customer's currency  """  
      self.TotActMaterial:int = obj["TotActMaterial"]
      """  Total Actual Material Amount  """  
      self.DocTotActMaterial:int = obj["DocTotActMaterial"]
      """  Total Actual Material Amount in customer's currency  """  
      self.TotActSubcontract:int = obj["TotActSubcontract"]
      """  Total Actual Subcontract Amount  """  
      self.DocTotActSubcontract:int = obj["DocTotActSubcontract"]
      """  Total Actual Subcontract Amount in  customer's currency  """  
      self.TotActMisc:int = obj["TotActMisc"]
      """  Total Actual Miscellaneous Amount  """  
      self.DocTotActMisc:int = obj["DocTotActMisc"]
      """  Total Actual Miscellaneous Amount in customer's currency  """  
      self.TotActCall:int = obj["TotActCall"]
      """  Total Actual Call Amount  """  
      self.DocTotActCall:int = obj["DocTotActCall"]
      """  Total Actual Call Amount in customer's curreny  """  
      self.TotBillMaterial:int = obj["TotBillMaterial"]
      """  Total Billable Material Amount  """  
      self.DocTotBillMaterial:int = obj["DocTotBillMaterial"]
      """  Total Billable Material Amount in customer's currency  """  
      self.TotBillSubcontract:int = obj["TotBillSubcontract"]
      """  Total Billable Subcontract Amount  """  
      self.DocTotBillSubcontract:int = obj["DocTotBillSubcontract"]
      """  Total Billable Subcontract Amount in customer's currency  """  
      self.TotBillMisc:int = obj["TotBillMisc"]
      """  Total Billable Miscellaneous Amount  """  
      self.DocTotBillMisc:int = obj["DocTotBillMisc"]
      """  Total Billable Miscellaneous Amount  """  
      self.TotBillCall:int = obj["TotBillCall"]
      """  Total Billable Call Amount  """  
      self.DocTotBillCall:int = obj["DocTotBillCall"]
      """  Total Billable Call Amount in customer's currency  """  
      self.DispEntryTime:str = obj["DispEntryTime"]
      self.DispRequestTime:str = obj["DispRequestTime"]
      self.DispSchedTime:str = obj["DispSchedTime"]
      self.DispActualTime:str = obj["DispActualTime"]
      self.TotEstLabor:int = obj["TotEstLabor"]
      """  Total Estimated Labor (Service) Amount  """  
      self.DocTotEstLabor:int = obj["DocTotEstLabor"]
      """  Total Estimated Labor (Service) Amount in customer's currency  """  
      self.TotActLabor:int = obj["TotActLabor"]
      """  Total Actual Labor (Service) Amount  """  
      self.DocTotActLabor:int = obj["DocTotActLabor"]
      """  Total Actual Labor (Service) Amount in customer's currency  """  
      self.TotBillLabor:int = obj["TotBillLabor"]
      """  Total Billable Labor (Service) Amount  """  
      self.DocTotBillLabor:int = obj["DocTotBillLabor"]
      """  Total Billable Labor (Service) Amount in customer's currency  """  
      self.EnableCallType:bool = obj["EnableCallType"]
      """  Indicates if the Call Type Code field needs to be enabled.  """  
      self.EnableServiceCall:bool = obj["EnableServiceCall"]
      """  Indicates if the user can maintain a service call header/line.  """  
      self.EnableCustTracker:bool = obj["EnableCustTracker"]
      """  Indicates if the user can view customer tracker.  """  
      self.EnableJobEntry:bool = obj["EnableJobEntry"]
      """  Indicates if the user can create/update a service call job.  """  
      self.EnableLaborEntry:bool = obj["EnableLaborEntry"]
      """  Indicates if the user can access labor entry screen.  """  
      self.EnableMiscShip:bool = obj["EnableMiscShip"]
      """  Indicates if the user can access the Miscellaneous Shipment screen.  """  
      self.EnableIssueMtl:bool = obj["EnableIssueMtl"]
      """  Indicates if the user can access Issue Material screen.  """  
      self.EnableIssueReturn:bool = obj["EnableIssueReturn"]
      """  Indicates if the user can access Issue Return screen.  """  
      self.EnableReopenCall:bool = obj["EnableReopenCall"]
      """  Indicates if the Reopen Service Call option should be enabled.  """  
      self.CustOnCreditHold:bool = obj["CustOnCreditHold"]
      """  Indicates if the customer on credit hold.  """  
      self.ShipEMailAddress:str = obj["ShipEMailAddress"]
      self.CustEMailAddress:str = obj["CustEMailAddress"]
      self.Rpt1TotActCall:int = obj["Rpt1TotActCall"]
      self.Rpt2TotActCall:int = obj["Rpt2TotActCall"]
      self.Rpt3TotActCall:int = obj["Rpt3TotActCall"]
      self.Rpt1TotActLabor:int = obj["Rpt1TotActLabor"]
      self.Rpt2TotActLabor:int = obj["Rpt2TotActLabor"]
      self.Rpt3TotActLabor:int = obj["Rpt3TotActLabor"]
      self.Rpt1TotActMaterial:int = obj["Rpt1TotActMaterial"]
      self.Rpt2TotActMaterial:int = obj["Rpt2TotActMaterial"]
      self.Rpt3TotActMaterial:int = obj["Rpt3TotActMaterial"]
      self.Rpt1TotActMisc:int = obj["Rpt1TotActMisc"]
      self.Rpt2TotActMisc:int = obj["Rpt2TotActMisc"]
      self.Rpt3TotActMisc:int = obj["Rpt3TotActMisc"]
      self.Rpt1TotActSubcontract:int = obj["Rpt1TotActSubcontract"]
      self.Rpt2TotActSubcontract:int = obj["Rpt2TotActSubcontract"]
      self.Rpt3TotActSubcontract:int = obj["Rpt3TotActSubcontract"]
      self.Rpt1TotBillCall:int = obj["Rpt1TotBillCall"]
      self.Rpt2TotBillCall:int = obj["Rpt2TotBillCall"]
      self.Rpt3TotBillCall:int = obj["Rpt3TotBillCall"]
      self.Rpt1TotBillLabor:int = obj["Rpt1TotBillLabor"]
      self.Rpt2TotBillLabor:int = obj["Rpt2TotBillLabor"]
      self.Rpt3TotBillLabor:int = obj["Rpt3TotBillLabor"]
      self.Rpt1TotBillMaterial:int = obj["Rpt1TotBillMaterial"]
      self.Rpt2TotBillMaterial:int = obj["Rpt2TotBillMaterial"]
      self.Rpt3TotBillMaterial:int = obj["Rpt3TotBillMaterial"]
      self.Rpt1TotBillMisc:int = obj["Rpt1TotBillMisc"]
      self.Rpt2TotBillMisc:int = obj["Rpt2TotBillMisc"]
      self.Rpt3TotBillMisc:int = obj["Rpt3TotBillMisc"]
      self.Rpt1TotBillSubcontract:int = obj["Rpt1TotBillSubcontract"]
      self.Rpt2TotBillSubcontract:int = obj["Rpt2TotBillSubcontract"]
      self.Rpt3TotBillSubcontract:int = obj["Rpt3TotBillSubcontract"]
      self.Rpt1TotEstCall:int = obj["Rpt1TotEstCall"]
      self.Rpt2TotEstCall:int = obj["Rpt2TotEstCall"]
      self.Rpt3TotEstCall:int = obj["Rpt3TotEstCall"]
      self.Rpt1TotEstLabor:int = obj["Rpt1TotEstLabor"]
      self.Rpt2TotEstLabor:int = obj["Rpt2TotEstLabor"]
      self.Rpt3TotEstLabor:int = obj["Rpt3TotEstLabor"]
      self.Rpt1TotEstMaterial:int = obj["Rpt1TotEstMaterial"]
      self.Rpt2TotEstMaterial:int = obj["Rpt2TotEstMaterial"]
      self.Rpt3TotEstMaterial:int = obj["Rpt3TotEstMaterial"]
      self.Rpt1TotEstMisc:int = obj["Rpt1TotEstMisc"]
      self.Rpt2TotEstMisc:int = obj["Rpt2TotEstMisc"]
      self.Rpt3TotEstMisc:int = obj["Rpt3TotEstMisc"]
      self.Rpt1TotEstSubcontract:int = obj["Rpt1TotEstSubcontract"]
      self.Rpt2TotEstSubcontract:int = obj["Rpt2TotEstSubcontract"]
      self.Rpt3TotEstSubcontract:int = obj["Rpt3TotEstSubcontract"]
      self.CustAllowOTS:bool = obj["CustAllowOTS"]
      self.ShipToAddrList:str = obj["ShipToAddrList"]
      self.SoldToAddrList:str = obj["SoldToAddrList"]
      self.BTCustName:str = obj["BTCustName"]
      """  Bill To Customer Name  """  
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers.  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.CallCodeCallDescription:str = obj["CallCodeCallDescription"]
      """  Description of the Call Type Code.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrRateGrpDescription:str = obj["CurrRateGrpDescription"]
      """  Description  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustNumAllowShipTo3:bool = obj["CustNumAllowShipTo3"]
      """  When yes, a ShipTo CustID on certain forms will be enabled. This allows a shipto of a different customer to be referenced as a 3rd party for a document.  """  
      self.OTSCountryNumDescription:str = obj["OTSCountryNumDescription"]
      """  Country name  """  
      self.OTSTaxRegionCodeDescription:str = obj["OTSTaxRegionCodeDescription"]
      """  Full description for the Tax Region.  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.ShipToName:str = obj["ShipToName"]
      """  The full name of the customer.  """  
      self.ShipToBTName:str = obj["ShipToBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.ShipToCustID:str = obj["ShipToCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      """  Full description for the Sales Tax category.  """  
      self.Selected:bool = obj["Selected"]
      """  Boolean for selection of FSCallhdList  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSCallhdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CallNum:int = obj["CallNum"]
      """  When creating a new Service Call the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the Service Call is for.  This must be valid in the Customer table.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Customer Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used  for the Service Call. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Establishes the Shipping Contact to be used.  In this case the contact at the location where the item the service call is covering are. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  """  
      self.EntryDate:str = obj["EntryDate"]
      """  defaults to TODAY  """  
      self.EntryTime:int = obj["EntryTime"]
      """  Time in second past midnight  """  
      self.RequestDate:str = obj["RequestDate"]
      """  The date that the service is requested for.  """  
      self.RequestTime:int = obj["RequestTime"]
      """  Time in second past midnight  """  
      self.SchedDate:str = obj["SchedDate"]
      """  The date that the service is scheduled for.  """  
      self.SchedTime:int = obj["SchedTime"]
      """  Time in second past midnight  """  
      self.ActualDate:str = obj["ActualDate"]
      """  The date that the service was performed on.  """  
      self.ActualTime:int = obj["ActualTime"]
      """  Time in second past midnight  """  
      self.CallComment:str = obj["CallComment"]
      """  Contains comments about the overall Call. These will be printed on the Service Call.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Contains comments about the overall Call. These will be printed on the Service Call invoice.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this Call.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.OpenCall:bool = obj["OpenCall"]
      """  Indicate that the call is open.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates that the call is closed and can be invoiced.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Indicated the invoice processing has been done for this call.  """  
      self.VoidCall:bool = obj["VoidCall"]
      """  No information can be entered when this flag is set. It won't be invoiced, labor and materials cannot be entered.  """  
      self.CallPriority:str = obj["CallPriority"]
      """  Can have 3 values High, normal and, Low  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as one of the selection parameters on the Service call entry edit reports. The intent is for users to be able to select Contract that they have entered for hard copy edit.
On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  """  
      self.CallCode:str = obj["CallCode"]
      """  A unique code that identifies the type of service call  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record.  """  
      self.LaborComplete:bool = obj["LaborComplete"]
      """   Set from labor entry.  Indicates that all labor has been entered for this call.  if this flag and the Material complete flag are set then the
opencall field will be set to FALSE and the READY TO INVOICE flag will be set o TRUE.  """  
      self.MaterialComplete:bool = obj["MaterialComplete"]
      """  Set from Issue materials.  Indicates that all material have been issued for this call.  if this flag and the Labor complete flag are set then the opencall field will be set to FALSE and the READY TO INVOICE flag will be set to TRUE.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Duration:int = obj["Duration"]
      """  The estimated duration of the service call in days.  """  
      self.CLCallNum:str = obj["CLCallNum"]
      """  The Clientele call number that is related to this call.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this service call.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping country number  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PONum:str = obj["PONum"]
      """  PONum  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the service call has to be synchronized with Epicor FSA application.  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers.  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for currency "BASE"  """  
      self.BTCustName:str = obj["BTCustName"]
      """  Bill To Customer Name  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currency Switch  """  
      self.CustAllowOTS:bool = obj["CustAllowOTS"]
      self.CustConName:str = obj["CustConName"]
      """  Customer Contact Name  """  
      self.CustEMailAddress:str = obj["CustEMailAddress"]
      self.CustFaxNum:str = obj["CustFaxNum"]
      """  Customer Fax Number  """  
      self.CustOnCreditHold:bool = obj["CustOnCreditHold"]
      """  Indicates if the customer on credit hold.  """  
      self.CustPhoneNum:str = obj["CustPhoneNum"]
      """  Customer Phone Number  """  
      self.DispActualTime:str = obj["DispActualTime"]
      self.DispEntryTime:str = obj["DispEntryTime"]
      self.DispRequestTime:str = obj["DispRequestTime"]
      self.DispSchedTime:str = obj["DispSchedTime"]
      self.DocTotActCall:int = obj["DocTotActCall"]
      """  Total Actual Call Amount in customer's curreny  """  
      self.DocTotActLabor:int = obj["DocTotActLabor"]
      """  Total Actual Labor (Service) Amount in customer's currency  """  
      self.DocTotActMaterial:int = obj["DocTotActMaterial"]
      """  Total Actual Material Amount in customer's currency  """  
      self.DocTotActMisc:int = obj["DocTotActMisc"]
      """  Total Actual Miscellaneous Amount in customer's currency  """  
      self.DocTotActSubcontract:int = obj["DocTotActSubcontract"]
      """  Total Actual Subcontract Amount in  customer's currency  """  
      self.DocTotBillCall:int = obj["DocTotBillCall"]
      """  Total Billable Call Amount in customer's currency  """  
      self.DocTotBillLabor:int = obj["DocTotBillLabor"]
      """  Total Billable Labor (Service) Amount in customer's currency  """  
      self.DocTotBillMaterial:int = obj["DocTotBillMaterial"]
      """  Total Billable Material Amount in customer's currency  """  
      self.DocTotBillMisc:int = obj["DocTotBillMisc"]
      """  Total Billable Miscellaneous Amount  """  
      self.DocTotBillSubcontract:int = obj["DocTotBillSubcontract"]
      """  Total Billable Subcontract Amount in customer's currency  """  
      self.DocTotEstCall:int = obj["DocTotEstCall"]
      """  Total Estimated Call Amount in customer's currency  """  
      self.DocTotEstLabor:int = obj["DocTotEstLabor"]
      """  Total Estimated Labor (Service) Amount in customer's currency  """  
      self.DocTotEstMaterial:int = obj["DocTotEstMaterial"]
      """  Total Estimated Mateiral Amount in customer's currency  """  
      self.DocTotEstMisc:int = obj["DocTotEstMisc"]
      """  Total Estimated Miscellaneous Amount in customer's currency  """  
      self.DocTotEstSubcontract:int = obj["DocTotEstSubcontract"]
      """  Total Estimated Subcontract Amount in customer's currency  """  
      self.EnableCallType:bool = obj["EnableCallType"]
      """  Indicates if the Call Type Code field needs to be enabled.  """  
      self.EnableCustTracker:bool = obj["EnableCustTracker"]
      """  Indicates if the user can view customer tracker.  """  
      self.EnableIssueMtl:bool = obj["EnableIssueMtl"]
      """  Indicates if the user can access Issue Material screen.  """  
      self.EnableIssueReturn:bool = obj["EnableIssueReturn"]
      """  Indicates if the user can access Issue Return screen.  """  
      self.EnableJobEntry:bool = obj["EnableJobEntry"]
      """  Indicates if the user can create/update a service call job.  """  
      self.EnableLaborEntry:bool = obj["EnableLaborEntry"]
      """  Indicates if the user can access labor entry screen.  """  
      self.EnableMiscShip:bool = obj["EnableMiscShip"]
      """  Indicates if the user can access the Miscellaneous Shipment screen.  """  
      self.EnableReopenCall:bool = obj["EnableReopenCall"]
      """  Indicates if the Reopen Service Call option should be enabled.  """  
      self.EnableServiceCall:bool = obj["EnableServiceCall"]
      """  Indicates if the user can maintain a service call header/line.  """  
      self.Rpt1TotActCall:int = obj["Rpt1TotActCall"]
      self.Rpt1TotActLabor:int = obj["Rpt1TotActLabor"]
      self.Rpt1TotActMaterial:int = obj["Rpt1TotActMaterial"]
      self.Rpt1TotActMisc:int = obj["Rpt1TotActMisc"]
      self.Rpt1TotActSubcontract:int = obj["Rpt1TotActSubcontract"]
      self.Rpt1TotBillCall:int = obj["Rpt1TotBillCall"]
      self.Rpt1TotBillLabor:int = obj["Rpt1TotBillLabor"]
      self.Rpt1TotBillMaterial:int = obj["Rpt1TotBillMaterial"]
      self.Rpt1TotBillMisc:int = obj["Rpt1TotBillMisc"]
      self.Rpt1TotBillSubcontract:int = obj["Rpt1TotBillSubcontract"]
      self.Rpt1TotEstCall:int = obj["Rpt1TotEstCall"]
      self.Rpt1TotEstLabor:int = obj["Rpt1TotEstLabor"]
      self.Rpt1TotEstMaterial:int = obj["Rpt1TotEstMaterial"]
      self.Rpt1TotEstMisc:int = obj["Rpt1TotEstMisc"]
      self.Rpt1TotEstSubcontract:int = obj["Rpt1TotEstSubcontract"]
      self.Rpt2TotActCall:int = obj["Rpt2TotActCall"]
      self.Rpt2TotActLabor:int = obj["Rpt2TotActLabor"]
      self.Rpt2TotActMaterial:int = obj["Rpt2TotActMaterial"]
      self.Rpt2TotActMisc:int = obj["Rpt2TotActMisc"]
      self.Rpt2TotActSubcontract:int = obj["Rpt2TotActSubcontract"]
      self.Rpt2TotBillCall:int = obj["Rpt2TotBillCall"]
      self.Rpt2TotBillLabor:int = obj["Rpt2TotBillLabor"]
      self.Rpt2TotBillMaterial:int = obj["Rpt2TotBillMaterial"]
      self.Rpt2TotBillMisc:int = obj["Rpt2TotBillMisc"]
      self.Rpt2TotBillSubcontract:int = obj["Rpt2TotBillSubcontract"]
      self.Rpt2TotEstCall:int = obj["Rpt2TotEstCall"]
      self.Rpt2TotEstLabor:int = obj["Rpt2TotEstLabor"]
      self.Rpt2TotEstMaterial:int = obj["Rpt2TotEstMaterial"]
      self.Rpt2TotEstMisc:int = obj["Rpt2TotEstMisc"]
      self.Rpt2TotEstSubcontract:int = obj["Rpt2TotEstSubcontract"]
      self.Rpt3TotActCall:int = obj["Rpt3TotActCall"]
      self.Rpt3TotActLabor:int = obj["Rpt3TotActLabor"]
      self.Rpt3TotActMaterial:int = obj["Rpt3TotActMaterial"]
      self.Rpt3TotActMisc:int = obj["Rpt3TotActMisc"]
      self.Rpt3TotActSubcontract:int = obj["Rpt3TotActSubcontract"]
      self.Rpt3TotBillCall:int = obj["Rpt3TotBillCall"]
      self.Rpt3TotBillLabor:int = obj["Rpt3TotBillLabor"]
      self.Rpt3TotBillMaterial:int = obj["Rpt3TotBillMaterial"]
      self.Rpt3TotBillMisc:int = obj["Rpt3TotBillMisc"]
      self.Rpt3TotBillSubcontract:int = obj["Rpt3TotBillSubcontract"]
      self.Rpt3TotEstCall:int = obj["Rpt3TotEstCall"]
      self.Rpt3TotEstLabor:int = obj["Rpt3TotEstLabor"]
      self.Rpt3TotEstMaterial:int = obj["Rpt3TotEstMaterial"]
      self.Rpt3TotEstMisc:int = obj["Rpt3TotEstMisc"]
      self.Rpt3TotEstSubcontract:int = obj["Rpt3TotEstSubcontract"]
      self.ShipConName:str = obj["ShipConName"]
      """  ShipTo Contact Name  """  
      self.ShipEMailAddress:str = obj["ShipEMailAddress"]
      self.ShipFaxNum:str = obj["ShipFaxNum"]
      """  ShipTo Fax Number  """  
      self.ShipPhoneNum:str = obj["ShipPhoneNum"]
      """  ShipTo Phone Number  """  
      self.ShipToAddrList:str = obj["ShipToAddrList"]
      self.SoldToAddrList:str = obj["SoldToAddrList"]
      self.TotActCall:int = obj["TotActCall"]
      """  Total Actual Call Amount  """  
      self.TotActLabor:int = obj["TotActLabor"]
      """  Total Actual Labor (Service) Amount  """  
      self.TotActMaterial:int = obj["TotActMaterial"]
      """  Total Actual Material Amount  """  
      self.TotActMisc:int = obj["TotActMisc"]
      """  Total Actual Miscellaneous Amount  """  
      self.TotActSubcontract:int = obj["TotActSubcontract"]
      """  Total Actual Subcontract Amount  """  
      self.TotBillCall:int = obj["TotBillCall"]
      """  Total Billable Call Amount  """  
      self.TotBillLabor:int = obj["TotBillLabor"]
      """  Total Billable Labor (Service) Amount  """  
      self.TotBillMaterial:int = obj["TotBillMaterial"]
      """  Total Billable Material Amount  """  
      self.TotBillMisc:int = obj["TotBillMisc"]
      """  Total Billable Miscellaneous Amount  """  
      self.TotBillSubcontract:int = obj["TotBillSubcontract"]
      """  Total Billable Subcontract Amount  """  
      self.TotEstCall:int = obj["TotEstCall"]
      """  Total Estimated Call Amount  """  
      self.TotEstLabor:int = obj["TotEstLabor"]
      """  Total Estimated Labor (Service) Amount  """  
      self.TotEstMaterial:int = obj["TotEstMaterial"]
      """  Total Estimated Material Amount  """  
      self.TotEstMisc:int = obj["TotEstMisc"]
      """  Total Estimated Miscellaneous Amount  """  
      self.TotEstSubContract:int = obj["TotEstSubContract"]
      """  Total Estimated Subcontract Amount  """  
      self.XRateLabel:str = obj["XRateLabel"]
      """  Exchange Rate Label  """  
      self.Selected:bool = obj["Selected"]
      """  Boolean for selection of FSCallhd  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BTCustNumInactive:bool = obj["BTCustNumInactive"]
      self.CallCodeCallDescription:str = obj["CallCodeCallDescription"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrRateGrpDescription:str = obj["CurrRateGrpDescription"]
      self.CustNumInactive:bool = obj["CustNumInactive"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumAllowShipTo3:bool = obj["CustNumAllowShipTo3"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumName:str = obj["CustNumName"]
      self.HDCaseDescription:str = obj["HDCaseDescription"]
      self.OTSCountryNumEUMember:bool = obj["OTSCountryNumEUMember"]
      self.OTSCountryNumDescription:str = obj["OTSCountryNumDescription"]
      self.OTSCountryNumISOCode:str = obj["OTSCountryNumISOCode"]
      self.OTSTaxRegionCodeDescription:str = obj["OTSTaxRegionCodeDescription"]
      self.PlantName:str = obj["PlantName"]
      self.ShipToCustID:str = obj["ShipToCustID"]
      self.ShipToBTName:str = obj["ShipToBTName"]
      self.ShipToName:str = obj["ShipToName"]
      self.ShipToInactive:bool = obj["ShipToInactive"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FsTechRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CallNum:int = obj["CallNum"]
      """  The call number that the technician is assigned to.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Part of the unique for this table.  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID.  """  
      self.Name:str = obj["Name"]
      """  the name of the employee assigned to the service call.  """  
      self.OpenCall:bool = obj["OpenCall"]
      """  Indicate that the call is open.  Not directly maintainable.  This is a mirror image of FSCallHd.OpenCall and is maintained by the WRITE trigger of FSCallHd.  """  
      self.CnvEmpID:str = obj["CnvEmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CallPriority:str = obj["CallPriority"]
      """  Call Priority  """  
      self.CustID:str = obj["CustID"]
      self.ShipName:str = obj["ShipName"]
      self.Address1:str = obj["Address1"]
      self.City:str = obj["City"]
      self.State:str = obj["State"]
      self.RequestDate:str = obj["RequestDate"]
      self.RequestTime:str = obj["RequestTime"]
      """  Request Time in HH:MM display format  """  
      self.SchedDate:str = obj["SchedDate"]
      self.SchedTime:str = obj["SchedTime"]
      """  Scheduled Time in HH:MM display format  """  
      self.Duration:int = obj["Duration"]
      self.ShowOpenCall:bool = obj["ShowOpenCall"]
      """  Indicates if this record is to be displayed as open service call.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ActivateServiceCall_input:
   """ Required : 
   ipCallNum
   """  
   def __init__(self, obj):
      self.ipCallNum:int = obj["ipCallNum"]
      """  The Service Call Number to close  """  
      pass

class ActivateServiceCall_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["returnObj"]
      pass

class AssignTechnician_input:
   """ Required : 
   ipCallNum
   ipEmpID
   ds
   """  
   def __init__(self, obj):
      self.ipCallNum:int = obj["ipCallNum"]
      """  The Service Call Number  """  
      self.ipEmpID:str = obj["ipEmpID"]
      """  The Employee ID of the service technician  """  
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

class AssignTechnician_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeBTCustID_input:
   """ Required : 
   billToCustNum
   ds
   """  
   def __init__(self, obj):
      self.billToCustNum:int = obj["billToCustNum"]
      """  Proposed bill to custid  """  
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

class ChangeBTCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDtlContractLine_input:
   """ Required : 
   ipContractLine
   ds
   """  
   def __init__(self, obj):
      self.ipContractLine:int = obj["ipContractLine"]
      """  The proposed service contract line number  """  
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

class ChangeDtlContractLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDtlContractNum_input:
   """ Required : 
   ipContractNum
   ds
   """  
   def __init__(self, obj):
      self.ipContractNum:int = obj["ipContractNum"]
      """  The proposed service contract number  """  
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

class ChangeDtlContractNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDtlDropShipPackLine_input:
   """ Required : 
   ipDropShipPackLine
   ds
   """  
   def __init__(self, obj):
      self.ipDropShipPackLine:int = obj["ipDropShipPackLine"]
      """  The proposed drop shipment pack line number  """  
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

class ChangeDtlDropShipPackLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDtlDropShipPackSlip_input:
   """ Required : 
   ipDropShipPackSlip
   ds
   """  
   def __init__(self, obj):
      self.ipDropShipPackSlip:str = obj["ipDropShipPackSlip"]
      """  The proposed drop shipment pack slip  """  
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

class ChangeDtlDropShipPackSlip_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDtlPackLine_input:
   """ Required : 
   ipPackLine
   ds
   """  
   def __init__(self, obj):
      self.ipPackLine:int = obj["ipPackLine"]
      """  The proposed pack line number  """  
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

class ChangeDtlPackLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDtlPackNum_input:
   """ Required : 
   ipPackNum
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      """  The proposed pack ID  """  
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

class ChangeDtlPackNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDtlPartNum_input:
   """ Required : 
   ds
   uomCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      self.uomCode:str = obj["uomCode"]
      """  UOM Code (only used for Product Codes)  """  
      pass

class ChangeDtlPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDtlRevisionNum_input:
   """ Required : 
   ipRevNum
   ds
   """  
   def __init__(self, obj):
      self.ipRevNum:str = obj["ipRevNum"]
      """  The proposed Revision Number  """  
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

class ChangeDtlRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDtlSerialNum_input:
   """ Required : 
   ipPartNum
   ipSerialNum
   ds
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  The part number for the proposed serial number  """  
      self.ipSerialNum:str = obj["ipSerialNum"]
      """  The proposed serial number  """  
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

class ChangeDtlSerialNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDtlXPartNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

class ChangeDtlXPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSCallDtProjectID_input:
   """ Required : 
   proposedProjectID
   ds
   """  
   def __init__(self, obj):
      self.proposedProjectID:str = obj["proposedProjectID"]
      """  The proposed project id  """  
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

class ChangeFSCallDtProjectID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeHdrBillToContact_input:
   """ Required : 
   ipPrcConNum
   ds
   """  
   def __init__(self, obj):
      self.ipPrcConNum:int = obj["ipPrcConNum"]
      """  The proposed Customer Contact  """  
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

class ChangeHdrBillToContact_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeHdrCallCode_input:
   """ Required : 
   ipCallCode
   ds
   """  
   def __init__(self, obj):
      self.ipCallCode:str = obj["ipCallCode"]
      """  The proposed Service Call Type Code  """  
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

class ChangeHdrCallCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeHdrCurrencyCode_input:
   """ Required : 
   ipCurrencyCode
   ds
   """  
   def __init__(self, obj):
      self.ipCurrencyCode:str = obj["ipCurrencyCode"]
      """  The proposed Currency Code  """  
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

class ChangeHdrCurrencyCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeHdrCustID_input:
   """ Required : 
   ipCustID
   ds
   """  
   def __init__(self, obj):
      self.ipCustID:str = obj["ipCustID"]
      """  The proposed Customer ID  """  
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

class ChangeHdrCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeHdrHDCaseNum_input:
   """ Required : 
   ipHDCaseNum
   ds
   """  
   def __init__(self, obj):
      self.ipHDCaseNum:int = obj["ipHDCaseNum"]
      """  The proposed Case Number  """  
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

class ChangeHdrHDCaseNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeHdrRequestTime_input:
   """ Required : 
   ipRequestTime
   ds
   """  
   def __init__(self, obj):
      self.ipRequestTime:int = obj["ipRequestTime"]
      """  The proposed Request Time as integer (number of minutes past midnight)  """  
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

class ChangeHdrRequestTime_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeHdrSchedTime_input:
   """ Required : 
   ipSchedTime
   ds
   """  
   def __init__(self, obj):
      self.ipSchedTime:int = obj["ipSchedTime"]
      """  The proposed Request Time as integer (number of seconds past midnight)  """  
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

class ChangeHdrSchedTime_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeHdrShipToContact_input:
   """ Required : 
   ipShpConNum
   ds
   """  
   def __init__(self, obj):
      self.ipShpConNum:int = obj["ipShpConNum"]
      """  The proposed ShipTo Contact  """  
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

class ChangeHdrShipToContact_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeHdrShipToCustID_input:
   """ Required : 
   ipShipToCustID
   ds
   """  
   def __init__(self, obj):
      self.ipShipToCustID:str = obj["ipShipToCustID"]
      """  The proposed Ship To Customer ID  """  
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

class ChangeHdrShipToCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeHdrShipToNum_input:
   """ Required : 
   ipShipToNum
   ds
   """  
   def __init__(self, obj):
      self.ipShipToNum:str = obj["ipShipToNum"]
      """  The proposed Customer ShipTo Number  """  
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

class ChangeHdrShipToNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeHdrUseOTS_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

class ChangeHdrUseOTS_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeIssueTopics_input:
   """ Required : 
   topics
   ds
   """  
   def __init__(self, obj):
      self.topics:str = obj["topics"]
      """  Proposed topics string id  """  
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

class ChangeIssueTopics_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeResTopics_input:
   """ Required : 
   topics
   ds
   """  
   def __init__(self, obj):
      self.topics:str = obj["topics"]
      """  Proposed topics string id  """  
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

class ChangeResTopics_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckDtlSerialNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

class CheckDtlSerialNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckPrePartInfo_input:
   """ Required : 
   vPartNum
   vContractNum
   vPackNum
   """  
   def __init__(self, obj):
      self.vPartNum:str = obj["vPartNum"]
      """  The input-output part number to validate and it gets returned  """  
      self.vContractNum:int = obj["vContractNum"]
      """  The current Service Contract number associated with the call  """  
      self.vPackNum:int = obj["vPackNum"]
      """  The current Pack id associated with the call  """  
      pass

class CheckPrePartInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vPartNum:str = obj["parameters"]
      self.vContractMsg:str = obj["parameters"]
      self.vWarrantyMsg:str = obj["parameters"]
      self.vSubPartMsg:str = obj["parameters"]
      self.vSubAvail:bool = obj["vSubAvail"]
      self.vMsgType:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckRateGrpCode_input:
   """ Required : 
   ipRateGrpCode
   ds
   """  
   def __init__(self, obj):
      self.ipRateGrpCode:str = obj["ipRateGrpCode"]
      """  Currency Rate Group Code  """  
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

class CheckRateGrpCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CloseServiceCall_input:
   """ Required : 
   ipCallNum
   """  
   def __init__(self, obj):
      self.ipCallNum:int = obj["ipCallNum"]
      """  The Service Call Number to close  """  
      pass

class CloseServiceCall_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["returnObj"]
      pass

class CreateServiceCallJob_input:
   """ Required : 
   ipCallNum
   ipCallLine
   ds
   """  
   def __init__(self, obj):
      self.ipCallNum:int = obj["ipCallNum"]
      """  The Service Call Number to create the job for.  """  
      self.ipCallLine:int = obj["ipCallLine"]
      """  The Service Call Line Number to create the job for.  """  
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

class CreateServiceCallJob_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   callNum
   """  
   def __init__(self, obj):
      self.callNum:int = obj["callNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_FSCallCustTrkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  From FSCallhd.Company  """  
      self.CallNum:int = obj["CallNum"]
      """  From FSCallhd.CallNum  """  
      self.OpenCall:bool = obj["OpenCall"]
      """  From FSCallhd.OpenCall  """  
      self.CallPriority:str = obj["CallPriority"]
      """  From FSCallhd.CallPriority  """  
      self.RequestDate:str = obj["RequestDate"]
      """  From FSCallhd.RequestDate  """  
      self.SchedDate:str = obj["SchedDate"]
      """  From FSCallhd.SchedDate  """  
      self.ActualDate:str = obj["ActualDate"]
      """  From FSCallhd.ActualDate  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  From FSCallhd.ReadyToInvoice  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  From FSCallhd.Invoiced  """  
      self.VoidCall:bool = obj["VoidCall"]
      """  From FSCallhd.VoidCall  """  
      self.CallCode:str = obj["CallCode"]
      """  From FSCallhd.CallCode  """  
      self.CustNum:int = obj["CustNum"]
      """  From FSCallhd.CustNum  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  From FSCallhd.ShipToNum  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  From FSCallhd.ShpConNum  """  
      self.CallLine:int = obj["CallLine"]
      """  From FSCallDt.CallLine  """  
      self.PartNum:str = obj["PartNum"]
      """  From FSCallDt.PartNum  """  
      self.LineDesc:str = obj["LineDesc"]
      """  From FSCallDt.LineDesc  """  
      self.CallQty:int = obj["CallQty"]
      """  From FSCallDt.CallQty  """  
      self.ContractCode:str = obj["ContractCode"]
      """  From FSCallDt.ContractCode  """  
      self.CallCodeCallDescription:str = obj["CallCodeCallDescription"]
      """  from FSCallhd.CallCodeCallDescription  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  from FSCallDt.RevisionNum  """  
      self.XPartNum:str = obj["XPartNum"]
      """  from FSCallDt.XPartNum  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  from FSCallDt.XRevisionNum  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full customer's name.  """  
      self.ShipToName:str = obj["ShipToName"]
      """  The name for the ship to location.  """  
      self.CustID:str = obj["CustID"]
      """  The customer ID.  """  
      self.IUM:str = obj["IUM"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSCallCustTrkTableset:
   def __init__(self, obj):
      self.FSCallCustTrk:list[Erp_Tablesets_FSCallCustTrkRow] = obj["FSCallCustTrk"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FSCallDtAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CallNum:int = obj["CallNum"]
      self.CallLine:int = obj["CallLine"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSCallDtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CallNum:int = obj["CallNum"]
      """  When creating a new Service Call ,the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  """  
      self.CallLine:int = obj["CallLine"]
      """  This field along with Company and CallNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last FSCalPrt record for the Call and the adding 1 to it.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial number of the part being repaired.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  """  
      self.CallQty:int = obj["CallQty"]
      """  TotalCall Quantity for the line item.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this Service call is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  The packing slip line that holds the warranty information for this service call  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number if this item is under a contract  """  
      self.ContractLine:int = obj["ContractLine"]
      """  This is the contract line the relates to the item on the service call.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Contract  """  
      self.CallComment:str = obj["CallComment"]
      """  Contains comments about the Item in need of service. These will be printed on the ServiceCall.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the repaired item. These will copied into the Invoice detail file as defaults.  """  
      self.ProbReasonCode:str = obj["ProbReasonCode"]
      """  Problem reason code from the reason master table. type problem.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the xasyst.CallProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  """  
      self.MatCovered:bool = obj["MatCovered"]
      """  Are Material cost covered  """  
      self.LabCovered:bool = obj["LabCovered"]
      """  Is Labor Cost Covered  """  
      self.MiscCovered:bool = obj["MiscCovered"]
      """  Are misc. Costs Covered  """  
      self.TotLabor:int = obj["TotLabor"]
      """  total Labor Amount.  """  
      self.DocTotLabor:int = obj["DocTotLabor"]
      """  total Labor Amount. In customers currency  """  
      self.TotBillLabor:int = obj["TotBillLabor"]
      """  total Billable Labor Amount.  """  
      self.DocTotBillLabor:int = obj["DocTotBillLabor"]
      """  total Billable Labor Amount. In Customers currency.  """  
      self.TotMaterial:int = obj["TotMaterial"]
      """  total Material Amount.  """  
      self.DocTotMaterial:int = obj["DocTotMaterial"]
      """  total Material Amount. In Customers currency  """  
      self.TotBillMaterial:int = obj["TotBillMaterial"]
      """  total Billable Material Amount.  """  
      self.DocTotBillMaterial:int = obj["DocTotBillMaterial"]
      """  total Billable Material Amount. In Customers Currency.  """  
      self.TotMisc:int = obj["TotMisc"]
      """  total Misc. Amount.  """  
      self.DocTotMisc:int = obj["DocTotMisc"]
      """  total Misc. Amount. In customers currency.  """  
      self.TotBillableMisc:int = obj["TotBillableMisc"]
      """  total Billable Misc. Amount.  """  
      self.DocTotBillableMisc:int = obj["DocTotBillableMisc"]
      """  total Billable Misc. Amount. In customer's currency.  """  
      self.TotMaterialCost:int = obj["TotMaterialCost"]
      """  total Material Cost.  """  
      self.TotMiscCost:int = obj["TotMiscCost"]
      """  total Misc. Cost.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record that this FSCallDt record. Can be blank.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  Associates the Call Line record back its linked JobHead record.  Not directly maintainable.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.TotSubCont:int = obj["TotSubCont"]
      """  Total Subcontract Amount.  """  
      self.DocTotSubCont:int = obj["DocTotSubCont"]
      """  total Subcontract Amount. In customers currency  """  
      self.TotBillSubCont:int = obj["TotBillSubCont"]
      """  total Billable Subcontract Amount.  """  
      self.DocTotBillSubCont:int = obj["DocTotBillSubCont"]
      """  total Billable Subcontract Amount. In Customers currency.  """  
      self.TotEstLabor:int = obj["TotEstLabor"]
      """  total Estimated Labor Amount.  """  
      self.DocTotEstLabor:int = obj["DocTotEstLabor"]
      """  total estimated Labor Amount. In customers currency  """  
      self.TotEstMaterial:int = obj["TotEstMaterial"]
      """  total Estimated Material Amount.  """  
      self.DocTotEstMaterial:int = obj["DocTotEstMaterial"]
      """  total Estimated Material Amount. In Customers currency  """  
      self.TotEstMisc:int = obj["TotEstMisc"]
      """  total Estimated Misc. Amount.  Future Use.  """  
      self.DocTotEstMisc:int = obj["DocTotEstMisc"]
      """  total Est. Misc. Amount. In customers currency. Future use  """  
      self.TotEstSubCont:int = obj["TotEstSubCont"]
      """  Total estimated Subcontract Amount.  """  
      self.DocTotEstSubCont:int = obj["DocTotEstSubCont"]
      """  total Estimated Subcontract Amount. In customers currency  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.Rpt1TotBillableMisc:int = obj["Rpt1TotBillableMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotBillableMisc:int = obj["Rpt2TotBillableMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotBillableMisc:int = obj["Rpt3TotBillableMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotBillLabor:int = obj["Rpt1TotBillLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotBillLabor:int = obj["Rpt2TotBillLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotBillLabor:int = obj["Rpt3TotBillLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotBillMaterial:int = obj["Rpt1TotBillMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotBillMaterial:int = obj["Rpt2TotBillMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotBillMaterial:int = obj["Rpt3TotBillMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotBillSubCont:int = obj["Rpt1TotBillSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotBillSubCont:int = obj["Rpt2TotBillSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotBillSubCont:int = obj["Rpt3TotBillSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotEstLabor:int = obj["Rpt1TotEstLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotEstLabor:int = obj["Rpt2TotEstLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotEstLabor:int = obj["Rpt3TotEstLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotEstMaterial:int = obj["Rpt1TotEstMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotEstMaterial:int = obj["Rpt2TotEstMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotEstMaterial:int = obj["Rpt3TotEstMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotEstMisc:int = obj["Rpt1TotEstMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotEstMisc:int = obj["Rpt2TotEstMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotEstMisc:int = obj["Rpt3TotEstMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotEstSubCont:int = obj["Rpt1TotEstSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotEstSubCont:int = obj["Rpt2TotEstSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotEstSubCont:int = obj["Rpt3TotEstSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotLabor:int = obj["Rpt1TotLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotLabor:int = obj["Rpt2TotLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotLabor:int = obj["Rpt3TotLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotMaterial:int = obj["Rpt1TotMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotMaterial:int = obj["Rpt2TotMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotMaterial:int = obj["Rpt3TotMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotMisc:int = obj["Rpt1TotMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotMisc:int = obj["Rpt2TotMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotMisc:int = obj["Rpt3TotMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotSubCont:int = obj["Rpt1TotSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotSubCont:int = obj["Rpt2TotSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotSubCont:int = obj["Rpt3TotSubCont"]
      """  Reporting currency value of this field  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  The drop shipment packing slip number that this Service call is linked with  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  The drop shipment packing slip line that holds the warranty information for this service call  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier number of the drop shipment and part of the primary key of a drop shipment line.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The supplier purchase point id of the drop shipment and part of the primary key of a drop shipment line.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.POLine:str = obj["POLine"]
      """  POLine  """  
      self.IssueTopicID1:str = obj["IssueTopicID1"]
      """  IssueTopicID1  """  
      self.IssueTopicID2:str = obj["IssueTopicID2"]
      """  IssueTopicID2  """  
      self.IssueTopicID3:str = obj["IssueTopicID3"]
      """  IssueTopicID3  """  
      self.IssueTopicID4:str = obj["IssueTopicID4"]
      """  IssueTopicID4  """  
      self.IssueTopicID5:str = obj["IssueTopicID5"]
      """  IssueTopicID5  """  
      self.IssueTopicID6:str = obj["IssueTopicID6"]
      """  IssueTopicID6  """  
      self.IssueTopicID7:str = obj["IssueTopicID7"]
      """  IssueTopicID7  """  
      self.IssueTopicID8:str = obj["IssueTopicID8"]
      """  IssueTopicID8  """  
      self.IssueTopicID9:str = obj["IssueTopicID9"]
      """  IssueTopicID9  """  
      self.IssueTopicID10:str = obj["IssueTopicID10"]
      """  IssueTopicID10  """  
      self.IssueTopics:str = obj["IssueTopics"]
      """  IssueTopics  """  
      self.ResTopicID1:str = obj["ResTopicID1"]
      """  ResTopicID1  """  
      self.ResTopicID2:str = obj["ResTopicID2"]
      """  ResTopicID2  """  
      self.ResTopicID3:str = obj["ResTopicID3"]
      """  ResTopicID3  """  
      self.ResTopicID4:str = obj["ResTopicID4"]
      """  ResTopicID4  """  
      self.ResTopicID5:str = obj["ResTopicID5"]
      """  ResTopicID5  """  
      self.ResTopicID6:str = obj["ResTopicID6"]
      """  ResTopicID6  """  
      self.ResTopicID7:str = obj["ResTopicID7"]
      """  ResTopicID7  """  
      self.ResTopicID8:str = obj["ResTopicID8"]
      """  ResTopicID8  """  
      self.ResTopicID9:str = obj["ResTopicID9"]
      """  ResTopicID9  """  
      self.ResTopicID10:str = obj["ResTopicID10"]
      """  ResTopicID10  """  
      self.ResTopics:str = obj["ResTopics"]
      """  ResTopics  """  
      self.PartDescription:str = obj["PartDescription"]
      """  PartDescription  """  
      self.CommentText:str = obj["CommentText"]
      """  CommentText  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Indicates the invoice processing has been done for this call line.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates that the call line can be invoiced.  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol of the "BASE" currency  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DisplayContractType:str = obj["DisplayContractType"]
      self.DocCurrSymbol:str = obj["DocCurrSymbol"]
      """  Currency.CurrSymbol of the customer's currency  """  
      self.DocTotLineBillCall:int = obj["DocTotLineBillCall"]
      """  Total Billable Call Amount for the line in customer's currency  """  
      self.DocTotLineCall:int = obj["DocTotLineCall"]
      """  Total Actual Call Amount for the line in customer's currency  """  
      self.DocTotLineEstCall:int = obj["DocTotLineEstCall"]
      """  Total Estimated Call AMount for the line in customer's currency  """  
      self.EnableContract:bool = obj["EnableContract"]
      """  Indicates if Contract entry should be enabled.  """  
      self.EnableWarranty:bool = obj["EnableWarranty"]
      """  Indicates if Warranty entry should be enabled.  """  
      self.IUMDesc:str = obj["IUMDesc"]
      """  Unit of Measure Description  """  
      self.ProbReasonDesc:str = obj["ProbReasonDesc"]
      """  Reson Code Description  """  
      self.Rpt1TotLineBillCall:int = obj["Rpt1TotLineBillCall"]
      self.Rpt1TotLineCall:int = obj["Rpt1TotLineCall"]
      self.Rpt1TotLineEstCall:int = obj["Rpt1TotLineEstCall"]
      self.Rpt2TotLineBillCall:int = obj["Rpt2TotLineBillCall"]
      self.Rpt2TotLineCall:int = obj["Rpt2TotLineCall"]
      self.Rpt2TotLineEstCall:int = obj["Rpt2TotLineEstCall"]
      self.Rpt3TotLineBillCall:int = obj["Rpt3TotLineBillCall"]
      self.Rpt3TotLineCall:int = obj["Rpt3TotLineCall"]
      self.Rpt3TotLineEstCall:int = obj["Rpt3TotLineEstCall"]
      self.TotLineBillCall:int = obj["TotLineBillCall"]
      """  Total Billable Call Amount for the line  """  
      self.TotLineCall:int = obj["TotLineCall"]
      """  Total Actual Call Amount for the line  """  
      self.TotLineEstCall:int = obj["TotLineEstCall"]
      """  Total Estimated Call Amount for the line  """  
      self.JobClosed:bool = obj["JobClosed"]
      self.BitFlag:int = obj["BitFlag"]
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      self.ContractLineLineDesc:str = obj["ContractLineLineDesc"]
      self.DropShipDtlLineDesc:str = obj["DropShipDtlLineDesc"]
      self.IssueTopicID1Description:str = obj["IssueTopicID1Description"]
      self.IssueTopicID10Description:str = obj["IssueTopicID10Description"]
      self.IssueTopicID2Description:str = obj["IssueTopicID2Description"]
      self.IssueTopicID3Description:str = obj["IssueTopicID3Description"]
      self.IssueTopicID4Description:str = obj["IssueTopicID4Description"]
      self.IssueTopicID5Description:str = obj["IssueTopicID5Description"]
      self.IssueTopicID6Description:str = obj["IssueTopicID6Description"]
      self.IssueTopicID7Description:str = obj["IssueTopicID7Description"]
      self.IssueTopicID8Description:str = obj["IssueTopicID8Description"]
      self.IssueTopicID9Description:str = obj["IssueTopicID9Description"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.PackLineLineDesc:str = obj["PackLineLineDesc"]
      self.PackNumShipStatus:str = obj["PackNumShipStatus"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.ResTopicID1Description:str = obj["ResTopicID1Description"]
      self.ResTopicID10Description:str = obj["ResTopicID10Description"]
      self.ResTopicID2Description:str = obj["ResTopicID2Description"]
      self.ResTopicID3Description:str = obj["ResTopicID3Description"]
      self.ResTopicID4Description:str = obj["ResTopicID4Description"]
      self.ResTopicID5Description:str = obj["ResTopicID5Description"]
      self.ResTopicID6Description:str = obj["ResTopicID6Description"]
      self.ResTopicID7Description:str = obj["ResTopicID7Description"]
      self.ResTopicID8Description:str = obj["ResTopicID8Description"]
      self.ResTopicID9Description:str = obj["ResTopicID9Description"]
      self.WarrantyCodeWarrDescription:str = obj["WarrantyCodeWarrDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSCallhdAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CallNum:int = obj["CallNum"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSCallhdListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CallNum:int = obj["CallNum"]
      """  When creating a new Service Call the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the Service Call is for.  This must be valid in the Customer table.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Customer Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used  for the Service Call. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Establishes the Shipping Contact to be used.  In this case the contact at the location where the item the service call is covering are. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  """  
      self.EntryDate:str = obj["EntryDate"]
      """  defaults to TODAY  """  
      self.EntryTime:int = obj["EntryTime"]
      """  Time in second past midnight  """  
      self.RequestDate:str = obj["RequestDate"]
      """  The date that the service is requested for.  """  
      self.RequestTime:int = obj["RequestTime"]
      """  Time in second past midnight  """  
      self.SchedDate:str = obj["SchedDate"]
      """  The date that the service is scheduled for.  """  
      self.SchedTime:int = obj["SchedTime"]
      """  Time in second past midnight  """  
      self.ActualDate:str = obj["ActualDate"]
      """  The date that the service was performed on.  """  
      self.ActualTime:int = obj["ActualTime"]
      """  Time in second past midnight  """  
      self.CallComment:str = obj["CallComment"]
      """  Contains comments about the overall Call. These will be printed on the Service Call.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Contains comments about the overall Call. These will be printed on the Service Call invoice.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this Call.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.OpenCall:bool = obj["OpenCall"]
      """  Indicate that the call is open.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates that the call is closed and can be invoiced.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Indicated the invoice processing has been done for this call.  """  
      self.VoidCall:bool = obj["VoidCall"]
      """  No information can be entered when this flag is set. It won't be invoiced, labor and materials cannot be entered.  """  
      self.CallPriority:str = obj["CallPriority"]
      """  Can have 3 values High, normal and, Low  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as one of the selection parameters on the Service call entry edit reports. The intent is for users to be able to select Contract that they have entered for hard copy edit.
On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  """  
      self.CallCode:str = obj["CallCode"]
      """  A unique code that identifies the type of service call  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record.  """  
      self.LaborComplete:bool = obj["LaborComplete"]
      """   Set from labor entry.  Indicates that all labor has been entered for this call.  if this flag and the Material complete flag are set then the
opencall field will be set to FALSE and the READY TO INVOICE flag will be set o TRUE.  """  
      self.MaterialComplete:bool = obj["MaterialComplete"]
      """  Set from Issue materials.  Indicates that all material have been issued for this call.  if this flag and the Labor complete flag are set then the opencall field will be set to FALSE and the READY TO INVOICE flag will be set to TRUE.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Duration:int = obj["Duration"]
      """  The estimated duration of the service call in days.  """  
      self.CLCallNum:str = obj["CLCallNum"]
      """  The Clientele call number that is related to this call.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this service call.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping country number  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustConName:str = obj["CustConName"]
      """  Customer Contact Name  """  
      self.CustPhoneNum:str = obj["CustPhoneNum"]
      """  Customer Phone Number  """  
      self.CustFaxNum:str = obj["CustFaxNum"]
      """  Customer Fax Number  """  
      self.ShipConName:str = obj["ShipConName"]
      """  ShipTo Contact Name  """  
      self.ShipPhoneNum:str = obj["ShipPhoneNum"]
      """  ShipTo Phone Number  """  
      self.ShipFaxNum:str = obj["ShipFaxNum"]
      """  ShipTo Fax Number  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currency Switch  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for currency "BASE"  """  
      self.XRateLabel:str = obj["XRateLabel"]
      """  Exchange Rate Label  """  
      self.TotEstMaterial:int = obj["TotEstMaterial"]
      """  Total Estimated Material Amount  """  
      self.DocTotEstMaterial:int = obj["DocTotEstMaterial"]
      """  Total Estimated Mateiral Amount in customer's currency  """  
      self.TotEstSubContract:int = obj["TotEstSubContract"]
      """  Total Estimated Subcontract Amount  """  
      self.DocTotEstSubcontract:int = obj["DocTotEstSubcontract"]
      """  Total Estimated Subcontract Amount in customer's currency  """  
      self.TotEstMisc:int = obj["TotEstMisc"]
      """  Total Estimated Miscellaneous Amount  """  
      self.DocTotEstMisc:int = obj["DocTotEstMisc"]
      """  Total Estimated Miscellaneous Amount in customer's currency  """  
      self.TotEstCall:int = obj["TotEstCall"]
      """  Total Estimated Call Amount  """  
      self.DocTotEstCall:int = obj["DocTotEstCall"]
      """  Total Estimated Call Amount in customer's currency  """  
      self.TotActMaterial:int = obj["TotActMaterial"]
      """  Total Actual Material Amount  """  
      self.DocTotActMaterial:int = obj["DocTotActMaterial"]
      """  Total Actual Material Amount in customer's currency  """  
      self.TotActSubcontract:int = obj["TotActSubcontract"]
      """  Total Actual Subcontract Amount  """  
      self.DocTotActSubcontract:int = obj["DocTotActSubcontract"]
      """  Total Actual Subcontract Amount in  customer's currency  """  
      self.TotActMisc:int = obj["TotActMisc"]
      """  Total Actual Miscellaneous Amount  """  
      self.DocTotActMisc:int = obj["DocTotActMisc"]
      """  Total Actual Miscellaneous Amount in customer's currency  """  
      self.TotActCall:int = obj["TotActCall"]
      """  Total Actual Call Amount  """  
      self.DocTotActCall:int = obj["DocTotActCall"]
      """  Total Actual Call Amount in customer's curreny  """  
      self.TotBillMaterial:int = obj["TotBillMaterial"]
      """  Total Billable Material Amount  """  
      self.DocTotBillMaterial:int = obj["DocTotBillMaterial"]
      """  Total Billable Material Amount in customer's currency  """  
      self.TotBillSubcontract:int = obj["TotBillSubcontract"]
      """  Total Billable Subcontract Amount  """  
      self.DocTotBillSubcontract:int = obj["DocTotBillSubcontract"]
      """  Total Billable Subcontract Amount in customer's currency  """  
      self.TotBillMisc:int = obj["TotBillMisc"]
      """  Total Billable Miscellaneous Amount  """  
      self.DocTotBillMisc:int = obj["DocTotBillMisc"]
      """  Total Billable Miscellaneous Amount  """  
      self.TotBillCall:int = obj["TotBillCall"]
      """  Total Billable Call Amount  """  
      self.DocTotBillCall:int = obj["DocTotBillCall"]
      """  Total Billable Call Amount in customer's currency  """  
      self.DispEntryTime:str = obj["DispEntryTime"]
      self.DispRequestTime:str = obj["DispRequestTime"]
      self.DispSchedTime:str = obj["DispSchedTime"]
      self.DispActualTime:str = obj["DispActualTime"]
      self.TotEstLabor:int = obj["TotEstLabor"]
      """  Total Estimated Labor (Service) Amount  """  
      self.DocTotEstLabor:int = obj["DocTotEstLabor"]
      """  Total Estimated Labor (Service) Amount in customer's currency  """  
      self.TotActLabor:int = obj["TotActLabor"]
      """  Total Actual Labor (Service) Amount  """  
      self.DocTotActLabor:int = obj["DocTotActLabor"]
      """  Total Actual Labor (Service) Amount in customer's currency  """  
      self.TotBillLabor:int = obj["TotBillLabor"]
      """  Total Billable Labor (Service) Amount  """  
      self.DocTotBillLabor:int = obj["DocTotBillLabor"]
      """  Total Billable Labor (Service) Amount in customer's currency  """  
      self.EnableCallType:bool = obj["EnableCallType"]
      """  Indicates if the Call Type Code field needs to be enabled.  """  
      self.EnableServiceCall:bool = obj["EnableServiceCall"]
      """  Indicates if the user can maintain a service call header/line.  """  
      self.EnableCustTracker:bool = obj["EnableCustTracker"]
      """  Indicates if the user can view customer tracker.  """  
      self.EnableJobEntry:bool = obj["EnableJobEntry"]
      """  Indicates if the user can create/update a service call job.  """  
      self.EnableLaborEntry:bool = obj["EnableLaborEntry"]
      """  Indicates if the user can access labor entry screen.  """  
      self.EnableMiscShip:bool = obj["EnableMiscShip"]
      """  Indicates if the user can access the Miscellaneous Shipment screen.  """  
      self.EnableIssueMtl:bool = obj["EnableIssueMtl"]
      """  Indicates if the user can access Issue Material screen.  """  
      self.EnableIssueReturn:bool = obj["EnableIssueReturn"]
      """  Indicates if the user can access Issue Return screen.  """  
      self.EnableReopenCall:bool = obj["EnableReopenCall"]
      """  Indicates if the Reopen Service Call option should be enabled.  """  
      self.CustOnCreditHold:bool = obj["CustOnCreditHold"]
      """  Indicates if the customer on credit hold.  """  
      self.ShipEMailAddress:str = obj["ShipEMailAddress"]
      self.CustEMailAddress:str = obj["CustEMailAddress"]
      self.Rpt1TotActCall:int = obj["Rpt1TotActCall"]
      self.Rpt2TotActCall:int = obj["Rpt2TotActCall"]
      self.Rpt3TotActCall:int = obj["Rpt3TotActCall"]
      self.Rpt1TotActLabor:int = obj["Rpt1TotActLabor"]
      self.Rpt2TotActLabor:int = obj["Rpt2TotActLabor"]
      self.Rpt3TotActLabor:int = obj["Rpt3TotActLabor"]
      self.Rpt1TotActMaterial:int = obj["Rpt1TotActMaterial"]
      self.Rpt2TotActMaterial:int = obj["Rpt2TotActMaterial"]
      self.Rpt3TotActMaterial:int = obj["Rpt3TotActMaterial"]
      self.Rpt1TotActMisc:int = obj["Rpt1TotActMisc"]
      self.Rpt2TotActMisc:int = obj["Rpt2TotActMisc"]
      self.Rpt3TotActMisc:int = obj["Rpt3TotActMisc"]
      self.Rpt1TotActSubcontract:int = obj["Rpt1TotActSubcontract"]
      self.Rpt2TotActSubcontract:int = obj["Rpt2TotActSubcontract"]
      self.Rpt3TotActSubcontract:int = obj["Rpt3TotActSubcontract"]
      self.Rpt1TotBillCall:int = obj["Rpt1TotBillCall"]
      self.Rpt2TotBillCall:int = obj["Rpt2TotBillCall"]
      self.Rpt3TotBillCall:int = obj["Rpt3TotBillCall"]
      self.Rpt1TotBillLabor:int = obj["Rpt1TotBillLabor"]
      self.Rpt2TotBillLabor:int = obj["Rpt2TotBillLabor"]
      self.Rpt3TotBillLabor:int = obj["Rpt3TotBillLabor"]
      self.Rpt1TotBillMaterial:int = obj["Rpt1TotBillMaterial"]
      self.Rpt2TotBillMaterial:int = obj["Rpt2TotBillMaterial"]
      self.Rpt3TotBillMaterial:int = obj["Rpt3TotBillMaterial"]
      self.Rpt1TotBillMisc:int = obj["Rpt1TotBillMisc"]
      self.Rpt2TotBillMisc:int = obj["Rpt2TotBillMisc"]
      self.Rpt3TotBillMisc:int = obj["Rpt3TotBillMisc"]
      self.Rpt1TotBillSubcontract:int = obj["Rpt1TotBillSubcontract"]
      self.Rpt2TotBillSubcontract:int = obj["Rpt2TotBillSubcontract"]
      self.Rpt3TotBillSubcontract:int = obj["Rpt3TotBillSubcontract"]
      self.Rpt1TotEstCall:int = obj["Rpt1TotEstCall"]
      self.Rpt2TotEstCall:int = obj["Rpt2TotEstCall"]
      self.Rpt3TotEstCall:int = obj["Rpt3TotEstCall"]
      self.Rpt1TotEstLabor:int = obj["Rpt1TotEstLabor"]
      self.Rpt2TotEstLabor:int = obj["Rpt2TotEstLabor"]
      self.Rpt3TotEstLabor:int = obj["Rpt3TotEstLabor"]
      self.Rpt1TotEstMaterial:int = obj["Rpt1TotEstMaterial"]
      self.Rpt2TotEstMaterial:int = obj["Rpt2TotEstMaterial"]
      self.Rpt3TotEstMaterial:int = obj["Rpt3TotEstMaterial"]
      self.Rpt1TotEstMisc:int = obj["Rpt1TotEstMisc"]
      self.Rpt2TotEstMisc:int = obj["Rpt2TotEstMisc"]
      self.Rpt3TotEstMisc:int = obj["Rpt3TotEstMisc"]
      self.Rpt1TotEstSubcontract:int = obj["Rpt1TotEstSubcontract"]
      self.Rpt2TotEstSubcontract:int = obj["Rpt2TotEstSubcontract"]
      self.Rpt3TotEstSubcontract:int = obj["Rpt3TotEstSubcontract"]
      self.CustAllowOTS:bool = obj["CustAllowOTS"]
      self.ShipToAddrList:str = obj["ShipToAddrList"]
      self.SoldToAddrList:str = obj["SoldToAddrList"]
      self.BTCustName:str = obj["BTCustName"]
      """  Bill To Customer Name  """  
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers.  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.CallCodeCallDescription:str = obj["CallCodeCallDescription"]
      """  Description of the Call Type Code.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrRateGrpDescription:str = obj["CurrRateGrpDescription"]
      """  Description  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustNumAllowShipTo3:bool = obj["CustNumAllowShipTo3"]
      """  When yes, a ShipTo CustID on certain forms will be enabled. This allows a shipto of a different customer to be referenced as a 3rd party for a document.  """  
      self.OTSCountryNumDescription:str = obj["OTSCountryNumDescription"]
      """  Country name  """  
      self.OTSTaxRegionCodeDescription:str = obj["OTSTaxRegionCodeDescription"]
      """  Full description for the Tax Region.  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.ShipToName:str = obj["ShipToName"]
      """  The full name of the customer.  """  
      self.ShipToBTName:str = obj["ShipToBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.ShipToCustID:str = obj["ShipToCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      """  Full description for the Sales Tax category.  """  
      self.Selected:bool = obj["Selected"]
      """  Boolean for selection of FSCallhdList  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSCallhdListTableset:
   def __init__(self, obj):
      self.FSCallhdList:list[Erp_Tablesets_FSCallhdListRow] = obj["FSCallhdList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FSCallhdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CallNum:int = obj["CallNum"]
      """  When creating a new Service Call the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the Service Call is for.  This must be valid in the Customer table.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Customer Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used  for the Service Call. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Establishes the Shipping Contact to be used.  In this case the contact at the location where the item the service call is covering are. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  """  
      self.EntryDate:str = obj["EntryDate"]
      """  defaults to TODAY  """  
      self.EntryTime:int = obj["EntryTime"]
      """  Time in second past midnight  """  
      self.RequestDate:str = obj["RequestDate"]
      """  The date that the service is requested for.  """  
      self.RequestTime:int = obj["RequestTime"]
      """  Time in second past midnight  """  
      self.SchedDate:str = obj["SchedDate"]
      """  The date that the service is scheduled for.  """  
      self.SchedTime:int = obj["SchedTime"]
      """  Time in second past midnight  """  
      self.ActualDate:str = obj["ActualDate"]
      """  The date that the service was performed on.  """  
      self.ActualTime:int = obj["ActualTime"]
      """  Time in second past midnight  """  
      self.CallComment:str = obj["CallComment"]
      """  Contains comments about the overall Call. These will be printed on the Service Call.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Contains comments about the overall Call. These will be printed on the Service Call invoice.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this Call.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.OpenCall:bool = obj["OpenCall"]
      """  Indicate that the call is open.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates that the call is closed and can be invoiced.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Indicated the invoice processing has been done for this call.  """  
      self.VoidCall:bool = obj["VoidCall"]
      """  No information can be entered when this flag is set. It won't be invoiced, labor and materials cannot be entered.  """  
      self.CallPriority:str = obj["CallPriority"]
      """  Can have 3 values High, normal and, Low  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as one of the selection parameters on the Service call entry edit reports. The intent is for users to be able to select Contract that they have entered for hard copy edit.
On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  """  
      self.CallCode:str = obj["CallCode"]
      """  A unique code that identifies the type of service call  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record.  """  
      self.LaborComplete:bool = obj["LaborComplete"]
      """   Set from labor entry.  Indicates that all labor has been entered for this call.  if this flag and the Material complete flag are set then the
opencall field will be set to FALSE and the READY TO INVOICE flag will be set o TRUE.  """  
      self.MaterialComplete:bool = obj["MaterialComplete"]
      """  Set from Issue materials.  Indicates that all material have been issued for this call.  if this flag and the Labor complete flag are set then the opencall field will be set to FALSE and the READY TO INVOICE flag will be set to TRUE.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Duration:int = obj["Duration"]
      """  The estimated duration of the service call in days.  """  
      self.CLCallNum:str = obj["CLCallNum"]
      """  The Clientele call number that is related to this call.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this service call.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping country number  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PONum:str = obj["PONum"]
      """  PONum  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the service call has to be synchronized with Epicor FSA application.  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers.  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for currency "BASE"  """  
      self.BTCustName:str = obj["BTCustName"]
      """  Bill To Customer Name  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currency Switch  """  
      self.CustAllowOTS:bool = obj["CustAllowOTS"]
      self.CustConName:str = obj["CustConName"]
      """  Customer Contact Name  """  
      self.CustEMailAddress:str = obj["CustEMailAddress"]
      self.CustFaxNum:str = obj["CustFaxNum"]
      """  Customer Fax Number  """  
      self.CustOnCreditHold:bool = obj["CustOnCreditHold"]
      """  Indicates if the customer on credit hold.  """  
      self.CustPhoneNum:str = obj["CustPhoneNum"]
      """  Customer Phone Number  """  
      self.DispActualTime:str = obj["DispActualTime"]
      self.DispEntryTime:str = obj["DispEntryTime"]
      self.DispRequestTime:str = obj["DispRequestTime"]
      self.DispSchedTime:str = obj["DispSchedTime"]
      self.DocTotActCall:int = obj["DocTotActCall"]
      """  Total Actual Call Amount in customer's curreny  """  
      self.DocTotActLabor:int = obj["DocTotActLabor"]
      """  Total Actual Labor (Service) Amount in customer's currency  """  
      self.DocTotActMaterial:int = obj["DocTotActMaterial"]
      """  Total Actual Material Amount in customer's currency  """  
      self.DocTotActMisc:int = obj["DocTotActMisc"]
      """  Total Actual Miscellaneous Amount in customer's currency  """  
      self.DocTotActSubcontract:int = obj["DocTotActSubcontract"]
      """  Total Actual Subcontract Amount in  customer's currency  """  
      self.DocTotBillCall:int = obj["DocTotBillCall"]
      """  Total Billable Call Amount in customer's currency  """  
      self.DocTotBillLabor:int = obj["DocTotBillLabor"]
      """  Total Billable Labor (Service) Amount in customer's currency  """  
      self.DocTotBillMaterial:int = obj["DocTotBillMaterial"]
      """  Total Billable Material Amount in customer's currency  """  
      self.DocTotBillMisc:int = obj["DocTotBillMisc"]
      """  Total Billable Miscellaneous Amount  """  
      self.DocTotBillSubcontract:int = obj["DocTotBillSubcontract"]
      """  Total Billable Subcontract Amount in customer's currency  """  
      self.DocTotEstCall:int = obj["DocTotEstCall"]
      """  Total Estimated Call Amount in customer's currency  """  
      self.DocTotEstLabor:int = obj["DocTotEstLabor"]
      """  Total Estimated Labor (Service) Amount in customer's currency  """  
      self.DocTotEstMaterial:int = obj["DocTotEstMaterial"]
      """  Total Estimated Mateiral Amount in customer's currency  """  
      self.DocTotEstMisc:int = obj["DocTotEstMisc"]
      """  Total Estimated Miscellaneous Amount in customer's currency  """  
      self.DocTotEstSubcontract:int = obj["DocTotEstSubcontract"]
      """  Total Estimated Subcontract Amount in customer's currency  """  
      self.EnableCallType:bool = obj["EnableCallType"]
      """  Indicates if the Call Type Code field needs to be enabled.  """  
      self.EnableCustTracker:bool = obj["EnableCustTracker"]
      """  Indicates if the user can view customer tracker.  """  
      self.EnableIssueMtl:bool = obj["EnableIssueMtl"]
      """  Indicates if the user can access Issue Material screen.  """  
      self.EnableIssueReturn:bool = obj["EnableIssueReturn"]
      """  Indicates if the user can access Issue Return screen.  """  
      self.EnableJobEntry:bool = obj["EnableJobEntry"]
      """  Indicates if the user can create/update a service call job.  """  
      self.EnableLaborEntry:bool = obj["EnableLaborEntry"]
      """  Indicates if the user can access labor entry screen.  """  
      self.EnableMiscShip:bool = obj["EnableMiscShip"]
      """  Indicates if the user can access the Miscellaneous Shipment screen.  """  
      self.EnableReopenCall:bool = obj["EnableReopenCall"]
      """  Indicates if the Reopen Service Call option should be enabled.  """  
      self.EnableServiceCall:bool = obj["EnableServiceCall"]
      """  Indicates if the user can maintain a service call header/line.  """  
      self.Rpt1TotActCall:int = obj["Rpt1TotActCall"]
      self.Rpt1TotActLabor:int = obj["Rpt1TotActLabor"]
      self.Rpt1TotActMaterial:int = obj["Rpt1TotActMaterial"]
      self.Rpt1TotActMisc:int = obj["Rpt1TotActMisc"]
      self.Rpt1TotActSubcontract:int = obj["Rpt1TotActSubcontract"]
      self.Rpt1TotBillCall:int = obj["Rpt1TotBillCall"]
      self.Rpt1TotBillLabor:int = obj["Rpt1TotBillLabor"]
      self.Rpt1TotBillMaterial:int = obj["Rpt1TotBillMaterial"]
      self.Rpt1TotBillMisc:int = obj["Rpt1TotBillMisc"]
      self.Rpt1TotBillSubcontract:int = obj["Rpt1TotBillSubcontract"]
      self.Rpt1TotEstCall:int = obj["Rpt1TotEstCall"]
      self.Rpt1TotEstLabor:int = obj["Rpt1TotEstLabor"]
      self.Rpt1TotEstMaterial:int = obj["Rpt1TotEstMaterial"]
      self.Rpt1TotEstMisc:int = obj["Rpt1TotEstMisc"]
      self.Rpt1TotEstSubcontract:int = obj["Rpt1TotEstSubcontract"]
      self.Rpt2TotActCall:int = obj["Rpt2TotActCall"]
      self.Rpt2TotActLabor:int = obj["Rpt2TotActLabor"]
      self.Rpt2TotActMaterial:int = obj["Rpt2TotActMaterial"]
      self.Rpt2TotActMisc:int = obj["Rpt2TotActMisc"]
      self.Rpt2TotActSubcontract:int = obj["Rpt2TotActSubcontract"]
      self.Rpt2TotBillCall:int = obj["Rpt2TotBillCall"]
      self.Rpt2TotBillLabor:int = obj["Rpt2TotBillLabor"]
      self.Rpt2TotBillMaterial:int = obj["Rpt2TotBillMaterial"]
      self.Rpt2TotBillMisc:int = obj["Rpt2TotBillMisc"]
      self.Rpt2TotBillSubcontract:int = obj["Rpt2TotBillSubcontract"]
      self.Rpt2TotEstCall:int = obj["Rpt2TotEstCall"]
      self.Rpt2TotEstLabor:int = obj["Rpt2TotEstLabor"]
      self.Rpt2TotEstMaterial:int = obj["Rpt2TotEstMaterial"]
      self.Rpt2TotEstMisc:int = obj["Rpt2TotEstMisc"]
      self.Rpt2TotEstSubcontract:int = obj["Rpt2TotEstSubcontract"]
      self.Rpt3TotActCall:int = obj["Rpt3TotActCall"]
      self.Rpt3TotActLabor:int = obj["Rpt3TotActLabor"]
      self.Rpt3TotActMaterial:int = obj["Rpt3TotActMaterial"]
      self.Rpt3TotActMisc:int = obj["Rpt3TotActMisc"]
      self.Rpt3TotActSubcontract:int = obj["Rpt3TotActSubcontract"]
      self.Rpt3TotBillCall:int = obj["Rpt3TotBillCall"]
      self.Rpt3TotBillLabor:int = obj["Rpt3TotBillLabor"]
      self.Rpt3TotBillMaterial:int = obj["Rpt3TotBillMaterial"]
      self.Rpt3TotBillMisc:int = obj["Rpt3TotBillMisc"]
      self.Rpt3TotBillSubcontract:int = obj["Rpt3TotBillSubcontract"]
      self.Rpt3TotEstCall:int = obj["Rpt3TotEstCall"]
      self.Rpt3TotEstLabor:int = obj["Rpt3TotEstLabor"]
      self.Rpt3TotEstMaterial:int = obj["Rpt3TotEstMaterial"]
      self.Rpt3TotEstMisc:int = obj["Rpt3TotEstMisc"]
      self.Rpt3TotEstSubcontract:int = obj["Rpt3TotEstSubcontract"]
      self.ShipConName:str = obj["ShipConName"]
      """  ShipTo Contact Name  """  
      self.ShipEMailAddress:str = obj["ShipEMailAddress"]
      self.ShipFaxNum:str = obj["ShipFaxNum"]
      """  ShipTo Fax Number  """  
      self.ShipPhoneNum:str = obj["ShipPhoneNum"]
      """  ShipTo Phone Number  """  
      self.ShipToAddrList:str = obj["ShipToAddrList"]
      self.SoldToAddrList:str = obj["SoldToAddrList"]
      self.TotActCall:int = obj["TotActCall"]
      """  Total Actual Call Amount  """  
      self.TotActLabor:int = obj["TotActLabor"]
      """  Total Actual Labor (Service) Amount  """  
      self.TotActMaterial:int = obj["TotActMaterial"]
      """  Total Actual Material Amount  """  
      self.TotActMisc:int = obj["TotActMisc"]
      """  Total Actual Miscellaneous Amount  """  
      self.TotActSubcontract:int = obj["TotActSubcontract"]
      """  Total Actual Subcontract Amount  """  
      self.TotBillCall:int = obj["TotBillCall"]
      """  Total Billable Call Amount  """  
      self.TotBillLabor:int = obj["TotBillLabor"]
      """  Total Billable Labor (Service) Amount  """  
      self.TotBillMaterial:int = obj["TotBillMaterial"]
      """  Total Billable Material Amount  """  
      self.TotBillMisc:int = obj["TotBillMisc"]
      """  Total Billable Miscellaneous Amount  """  
      self.TotBillSubcontract:int = obj["TotBillSubcontract"]
      """  Total Billable Subcontract Amount  """  
      self.TotEstCall:int = obj["TotEstCall"]
      """  Total Estimated Call Amount  """  
      self.TotEstLabor:int = obj["TotEstLabor"]
      """  Total Estimated Labor (Service) Amount  """  
      self.TotEstMaterial:int = obj["TotEstMaterial"]
      """  Total Estimated Material Amount  """  
      self.TotEstMisc:int = obj["TotEstMisc"]
      """  Total Estimated Miscellaneous Amount  """  
      self.TotEstSubContract:int = obj["TotEstSubContract"]
      """  Total Estimated Subcontract Amount  """  
      self.XRateLabel:str = obj["XRateLabel"]
      """  Exchange Rate Label  """  
      self.Selected:bool = obj["Selected"]
      """  Boolean for selection of FSCallhd  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BTCustNumInactive:bool = obj["BTCustNumInactive"]
      self.CallCodeCallDescription:str = obj["CallCodeCallDescription"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrRateGrpDescription:str = obj["CurrRateGrpDescription"]
      self.CustNumInactive:bool = obj["CustNumInactive"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumAllowShipTo3:bool = obj["CustNumAllowShipTo3"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumName:str = obj["CustNumName"]
      self.HDCaseDescription:str = obj["HDCaseDescription"]
      self.OTSCountryNumEUMember:bool = obj["OTSCountryNumEUMember"]
      self.OTSCountryNumDescription:str = obj["OTSCountryNumDescription"]
      self.OTSCountryNumISOCode:str = obj["OTSCountryNumISOCode"]
      self.OTSTaxRegionCodeDescription:str = obj["OTSTaxRegionCodeDescription"]
      self.PlantName:str = obj["PlantName"]
      self.ShipToCustID:str = obj["ShipToCustID"]
      self.ShipToBTName:str = obj["ShipToBTName"]
      self.ShipToName:str = obj["ShipToName"]
      self.ShipToInactive:bool = obj["ShipToInactive"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FsTechRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CallNum:int = obj["CallNum"]
      """  The call number that the technician is assigned to.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Part of the unique for this table.  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID.  """  
      self.Name:str = obj["Name"]
      """  the name of the employee assigned to the service call.  """  
      self.OpenCall:bool = obj["OpenCall"]
      """  Indicate that the call is open.  Not directly maintainable.  This is a mirror image of FSCallHd.OpenCall and is maintained by the WRITE trigger of FSCallHd.  """  
      self.CnvEmpID:str = obj["CnvEmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CallPriority:str = obj["CallPriority"]
      """  Call Priority  """  
      self.CustID:str = obj["CustID"]
      self.ShipName:str = obj["ShipName"]
      self.Address1:str = obj["Address1"]
      self.City:str = obj["City"]
      self.State:str = obj["State"]
      self.RequestDate:str = obj["RequestDate"]
      self.RequestTime:str = obj["RequestTime"]
      """  Request Time in HH:MM display format  """  
      self.SchedDate:str = obj["SchedDate"]
      self.SchedTime:str = obj["SchedTime"]
      """  Scheduled Time in HH:MM display format  """  
      self.Duration:int = obj["Duration"]
      self.ShowOpenCall:bool = obj["ShowOpenCall"]
      """  Indicates if this record is to be displayed as open service call.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ServiceCallCenterTableset:
   def __init__(self, obj):
      self.FSCallhd:list[Erp_Tablesets_FSCallhdRow] = obj["FSCallhd"]
      self.FSCallhdAttch:list[Erp_Tablesets_FSCallhdAttchRow] = obj["FSCallhdAttch"]
      self.FSCallDt:list[Erp_Tablesets_FSCallDtRow] = obj["FSCallDt"]
      self.FSCallDtAttch:list[Erp_Tablesets_FSCallDtAttchRow] = obj["FSCallDtAttch"]
      self.FsTech:list[Erp_Tablesets_FsTechRow] = obj["FsTech"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtServiceCallCenterTableset:
   def __init__(self, obj):
      self.FSCallhd:list[Erp_Tablesets_FSCallhdRow] = obj["FSCallhd"]
      self.FSCallhdAttch:list[Erp_Tablesets_FSCallhdAttchRow] = obj["FSCallhdAttch"]
      self.FSCallDt:list[Erp_Tablesets_FSCallDtRow] = obj["FSCallDt"]
      self.FSCallDtAttch:list[Erp_Tablesets_FSCallDtAttchRow] = obj["FSCallDtAttch"]
      self.FsTech:list[Erp_Tablesets_FsTechRow] = obj["FsTech"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExpireDate_input:
   """ Required : 
   ExpirationDate
   EffectiveDAte
   Duration
   modifier
   """  
   def __init__(self, obj):
      self.ExpirationDate:str = obj["ExpirationDate"]
      self.EffectiveDAte:str = obj["EffectiveDAte"]
      self.Duration:int = obj["Duration"]
      self.modifier:str = obj["modifier"]
      pass

class ExpireDate_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class FindPart_input:
   """ Required : 
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  PartNum  """  
      pass

class FindPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPartNum:str = obj["parameters"]
      self.opUOM:str = obj["parameters"]
      self.opMatchType:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   callNum
   """  
   def __init__(self, obj):
      self.callNum:int = obj["callNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  The table name  """  
      self.fieldName:str = obj["fieldName"]
      """  The field name.  """  
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetFSCallhdReadyForInvoice_input:
   """ Required : 
   custNums
   callCodes
   """  
   def __init__(self, obj):
      self.custNums:str = obj["custNums"]
      self.callCodes:str = obj["callCodes"]
      pass

class GetFSCallhdReadyForInvoice_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FSCallhdListTableset] = obj["returnObj"]
      pass

class GetListRemoveInvoiced_input:
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

class GetListRemoveInvoiced_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FSCallhdListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
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
      self.returnObj:list[Erp_Tablesets_FSCallhdListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewFSCallDtAttch_input:
   """ Required : 
   ds
   callNum
   callLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      self.callNum:int = obj["callNum"]
      self.callLine:int = obj["callLine"]
      pass

class GetNewFSCallDtAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFSCallDt_input:
   """ Required : 
   ds
   callNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      self.callNum:int = obj["callNum"]
      pass

class GetNewFSCallDt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFSCallHd1_input:
   """ Required : 
   ds
   ipCustNum
   ipShipToNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      self.ipCustNum:int = obj["ipCustNum"]
      """  The Customer Number for this Service Call  """  
      self.ipShipToNum:str = obj["ipShipToNum"]
      """  The Customer ShipTo Number for this Service Call  """  
      pass

class GetNewFSCallHd1_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFSCallhdAttch_input:
   """ Required : 
   ds
   callNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      self.callNum:int = obj["callNum"]
      pass

class GetNewFSCallhdAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFSCallhd_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

class GetNewFSCallhd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFsTech_input:
   """ Required : 
   ds
   callNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      self.callNum:int = obj["callNum"]
      pass

class GetNewFsTech_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPartFromRowID_input:
   """ Required : 
   ipRowType
   ipRowID
   """  
   def __init__(self, obj):
      self.ipRowType:str = obj["ipRowType"]
      """  Row Type  """  
      self.ipRowID:str = obj["ipRowID"]
      """  Row ID  """  
      pass

class GetPartFromRowID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPartNum:str = obj["parameters"]
      self.opUOM:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPartXRefInfo_input:
   """ Required : 
   partNum
   custNum
   uomCode
   SysRowID
   rowType
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Proposed PartNumber change  """  
      self.custNum:int = obj["custNum"]
      """  Customer number  """  
      self.uomCode:str = obj["uomCode"]
      """  UOM Code (only used for Product Codes)  """  
      self.SysRowID:str = obj["SysRowID"]
      """  RowID of the selected record. Skips find part logic if this has a value.  """  
      self.rowType:str = obj["rowType"]
      """  RowType of the selected record. Only used with sysRowID.  """  
      pass

class GetPartXRefInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partNum:str = obj["parameters"]
      self.uomCode:str = obj["parameters"]
      self.serialWarning:str = obj["parameters"]
      self.questionString:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      pass

      """  output parameters  """  

class GetRowsContactTracker_input:
   """ Required : 
   whereClauseFSCallhd
   whereClauseFSCallhdAttch
   whereClauseFSCallDt
   whereClauseFSCallDtAttch
   whereClauseFsTech
   contactName
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseFSCallhd:str = obj["whereClauseFSCallhd"]
      """  Whereclause for FSCallhd table.  """  
      self.whereClauseFSCallhdAttch:str = obj["whereClauseFSCallhdAttch"]
      """  Whereclause for FSCallhdAttch table.  """  
      self.whereClauseFSCallDt:str = obj["whereClauseFSCallDt"]
      """  Whereclause for FSCallDt table.  """  
      self.whereClauseFSCallDtAttch:str = obj["whereClauseFSCallDtAttch"]
      """  Whereclause for FSCallDtAttch table.  """  
      self.whereClauseFsTech:str = obj["whereClauseFsTech"]
      """  Whereclause for FsTech table.  """  
      self.contactName:str = obj["contactName"]
      """  Contact to return data for.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsContactTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FSCallCustTrkTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsCustomerTracker_input:
   """ Required : 
   whereClauseFSCallhd
   whereClauseFSCallhdAttch
   whereClauseFSCallDt
   whereClauseFSCallDtAttch
   whereClauseFsTech
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseFSCallhd:str = obj["whereClauseFSCallhd"]
      """  Whereclause for FSCallhd table.  """  
      self.whereClauseFSCallhdAttch:str = obj["whereClauseFSCallhdAttch"]
      """  Whereclause for FSCallhdAttch table.  """  
      self.whereClauseFSCallDt:str = obj["whereClauseFSCallDt"]
      """  Whereclause for FSCallDt table.  """  
      self.whereClauseFSCallDtAttch:str = obj["whereClauseFSCallDtAttch"]
      """  Whereclause for FSCallDtAttch table.  """  
      self.whereClauseFsTech:str = obj["whereClauseFsTech"]
      """  Whereclause for FsTech table.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsCustomerTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FSCallCustTrkTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseFSCallhd
   whereClauseFSCallhdAttch
   whereClauseFSCallDt
   whereClauseFSCallDtAttch
   whereClauseFsTech
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseFSCallhd:str = obj["whereClauseFSCallhd"]
      self.whereClauseFSCallhdAttch:str = obj["whereClauseFSCallhdAttch"]
      self.whereClauseFSCallDt:str = obj["whereClauseFSCallDt"]
      self.whereClauseFSCallDtAttch:str = obj["whereClauseFSCallDtAttch"]
      self.whereClauseFsTech:str = obj["whereClauseFsTech"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetXPartByPartNum_input:
   """ Required : 
   custNum
   partNum
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      """  Customer Number  """  
      self.partNum:str = obj["partNum"]
      """  Part Number  """  
      pass

class GetXPartByPartNum_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
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

class PreCloseServiceCall_input:
   """ Required : 
   ipCallNum
   """  
   def __init__(self, obj):
      self.ipCallNum:int = obj["ipCallNum"]
      """  The Service Call Number to close  """  
      pass

class PreCloseServiceCall_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ReopenServiceCall_input:
   """ Required : 
   ipCallNum
   """  
   def __init__(self, obj):
      self.ipCallNum:int = obj["ipCallNum"]
      """  The Service Call Number to close  """  
      pass

class ReopenServiceCall_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtServiceCallCenterTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtServiceCallCenterTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateOTSTaxID_input:
   """ Required : 
   ds
   manualValidation
   hmrcFraudPrevHeader
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      self.manualValidation:bool = obj["manualValidation"]
      """  bool  """  
      self.hmrcFraudPrevHeader:str = obj["hmrcFraudPrevHeader"]
      """  string  """  
      pass

class ValidateOTSTaxID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["ds"]
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class VoidServiceCall_input:
   """ Required : 
   ipCallNum
   """  
   def __init__(self, obj):
      self.ipCallNum:int = obj["ipCallNum"]
      """  The Service Call Number to close  """  
      pass

class VoidServiceCall_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ServiceCallCenterTableset] = obj["returnObj"]
      pass

