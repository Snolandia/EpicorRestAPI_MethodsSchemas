import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.EmpBasicSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_EmpBasics(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EmpBasics items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EmpBasics
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpBasicRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics",headers=creds) as resp:
           return await resp.json()

async def post_EmpBasics(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EmpBasics
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EmpBasicRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EmpBasicRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EmpBasics_Company_EmpID(Company, EmpID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EmpBasic item
   Description: Calls GetByID to retrieve the EmpBasic item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpBasic
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpBasicRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics(" + Company + "," + EmpID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EmpBasics_Company_EmpID(Company, EmpID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EmpBasic for the service
   Description: Calls UpdateExt to update EmpBasic. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EmpBasic
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EmpBasicRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics(" + Company + "," + EmpID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EmpBasics_Company_EmpID(Company, EmpID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EmpBasic item
   Description: Call UpdateExt to delete EmpBasic item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EmpBasic
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics(" + Company + "," + EmpID + ")",headers=creds) as resp:
           return await resp.json()

async def get_EmpBasics_Company_EmpID_EmpLabExpRates(Company, EmpID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EmpLabExpRates items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EmpLabExpRates1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpLabExpRateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics(" + Company + "," + EmpID + ")/EmpLabExpRates",headers=creds) as resp:
           return await resp.json()

async def get_EmpBasics_Company_EmpID_EmpLabExpRates_Company_EmpID_ExpenseCode(Company, EmpID, ExpenseCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EmpLabExpRate item
   Description: Calls GetByID to retrieve the EmpLabExpRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpLabExpRate1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param ExpenseCode: Desc: ExpenseCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpLabExpRateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics(" + Company + "," + EmpID + ")/EmpLabExpRates(" + Company + "," + EmpID + "," + ExpenseCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_EmpBasics_Company_EmpID_EmpCals(Company, EmpID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EmpCals items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EmpCals1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpCalRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics(" + Company + "," + EmpID + ")/EmpCals",headers=creds) as resp:
           return await resp.json()

async def get_EmpBasics_Company_EmpID_EmpCals_Company_EmpID_CalendarID_FromEffectiveDate(Company, EmpID, CalendarID, FromEffectiveDate, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EmpCal item
   Description: Calls GetByID to retrieve the EmpCal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpCal1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param CalendarID: Desc: CalendarID   Required: True   Allow empty value : True
      :param FromEffectiveDate: Desc: FromEffectiveDate   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpCalRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics(" + Company + "," + EmpID + ")/EmpCals(" + Company + "," + EmpID + "," + CalendarID + "," + FromEffectiveDate + ")",headers=creds) as resp:
           return await resp.json()

async def get_EmpBasics_Company_EmpID_ResourceCals(Company, EmpID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ResourceCals items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ResourceCals1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ResourceCalRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics(" + Company + "," + EmpID + ")/ResourceCals",headers=creds) as resp:
           return await resp.json()

async def get_EmpBasics_Company_EmpID_ResourceCals_Company_ResourceGrpID_ResourceID_SpecialDay(Company, EmpID, ResourceGrpID, ResourceID, SpecialDay, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ResourceCal item
   Description: Calls GetByID to retrieve the ResourceCal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ResourceCal1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param SpecialDay: Desc: SpecialDay   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ResourceCalRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics(" + Company + "," + EmpID + ")/ResourceCals(" + Company + "," + ResourceGrpID + "," + ResourceID + "," + SpecialDay + ")",headers=creds) as resp:
           return await resp.json()

async def get_EmpBasics_Company_EmpID_EmpRoles(Company, EmpID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EmpRoles items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EmpRoles1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpRoleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics(" + Company + "," + EmpID + ")/EmpRoles",headers=creds) as resp:
           return await resp.json()

async def get_EmpBasics_Company_EmpID_EmpRoles_Company_EmpID_RoleCd(Company, EmpID, RoleCd, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EmpRole item
   Description: Calls GetByID to retrieve the EmpRole item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpRole1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param RoleCd: Desc: RoleCd   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpRoleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics(" + Company + "," + EmpID + ")/EmpRoles(" + Company + "," + EmpID + "," + RoleCd + ")",headers=creds) as resp:
           return await resp.json()

async def get_EmpBasics_Company_EmpID_EntityGLCs(Company, EmpID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EntityGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EntityGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics(" + Company + "," + EmpID + ")/EntityGLCs",headers=creds) as resp:
           return await resp.json()

async def get_EmpBasics_Company_EmpID_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, EmpID, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics(" + Company + "," + EmpID + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_EmpBasics_Company_EmpID_EmpBasicAttches(Company, EmpID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EmpBasicAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EmpBasicAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpBasicAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics(" + Company + "," + EmpID + ")/EmpBasicAttches",headers=creds) as resp:
           return await resp.json()

async def get_EmpBasics_Company_EmpID_EmpBasicAttches_Company_EmpID_DrawingSeq(Company, EmpID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EmpBasicAttch item
   Description: Calls GetByID to retrieve the EmpBasicAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpBasicAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpBasicAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics(" + Company + "," + EmpID + ")/EmpBasicAttches(" + Company + "," + EmpID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_EmpLabExpRates(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EmpLabExpRates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EmpLabExpRates
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpLabExpRateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpLabExpRates",headers=creds) as resp:
           return await resp.json()

async def post_EmpLabExpRates(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EmpLabExpRates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EmpLabExpRateRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EmpLabExpRateRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpLabExpRates", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EmpLabExpRates_Company_EmpID_ExpenseCode(Company, EmpID, ExpenseCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EmpLabExpRate item
   Description: Calls GetByID to retrieve the EmpLabExpRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpLabExpRate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param ExpenseCode: Desc: ExpenseCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpLabExpRateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpLabExpRates(" + Company + "," + EmpID + "," + ExpenseCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EmpLabExpRates_Company_EmpID_ExpenseCode(Company, EmpID, ExpenseCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EmpLabExpRate for the service
   Description: Calls UpdateExt to update EmpLabExpRate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EmpLabExpRate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param ExpenseCode: Desc: ExpenseCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EmpLabExpRateRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpLabExpRates(" + Company + "," + EmpID + "," + ExpenseCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EmpLabExpRates_Company_EmpID_ExpenseCode(Company, EmpID, ExpenseCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EmpLabExpRate item
   Description: Call UpdateExt to delete EmpLabExpRate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EmpLabExpRate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param ExpenseCode: Desc: ExpenseCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpLabExpRates(" + Company + "," + EmpID + "," + ExpenseCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_EmpCals(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EmpCals items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EmpCals
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpCalRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpCals",headers=creds) as resp:
           return await resp.json()

async def post_EmpCals(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EmpCals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EmpCalRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EmpCalRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpCals", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EmpCals_Company_EmpID_CalendarID_FromEffectiveDate(Company, EmpID, CalendarID, FromEffectiveDate, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EmpCal item
   Description: Calls GetByID to retrieve the EmpCal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpCal
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param CalendarID: Desc: CalendarID   Required: True   Allow empty value : True
      :param FromEffectiveDate: Desc: FromEffectiveDate   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpCalRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpCals(" + Company + "," + EmpID + "," + CalendarID + "," + FromEffectiveDate + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EmpCals_Company_EmpID_CalendarID_FromEffectiveDate(Company, EmpID, CalendarID, FromEffectiveDate, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EmpCal for the service
   Description: Calls UpdateExt to update EmpCal. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EmpCal
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param CalendarID: Desc: CalendarID   Required: True   Allow empty value : True
      :param FromEffectiveDate: Desc: FromEffectiveDate   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EmpCalRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpCals(" + Company + "," + EmpID + "," + CalendarID + "," + FromEffectiveDate + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EmpCals_Company_EmpID_CalendarID_FromEffectiveDate(Company, EmpID, CalendarID, FromEffectiveDate, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EmpCal item
   Description: Call UpdateExt to delete EmpCal item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EmpCal
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param CalendarID: Desc: CalendarID   Required: True   Allow empty value : True
      :param FromEffectiveDate: Desc: FromEffectiveDate   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpCals(" + Company + "," + EmpID + "," + CalendarID + "," + FromEffectiveDate + ")",headers=creds) as resp:
           return await resp.json()

async def get_ResourceCals(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ResourceCals items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ResourceCals
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ResourceCalRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/ResourceCals",headers=creds) as resp:
           return await resp.json()

async def post_ResourceCals(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ResourceCals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ResourceCalRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ResourceCalRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/ResourceCals", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ResourceCals_Company_ResourceGrpID_ResourceID_SpecialDay(Company, ResourceGrpID, ResourceID, SpecialDay, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ResourceCal item
   Description: Calls GetByID to retrieve the ResourceCal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ResourceCal
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param SpecialDay: Desc: SpecialDay   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ResourceCalRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/ResourceCals(" + Company + "," + ResourceGrpID + "," + ResourceID + "," + SpecialDay + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ResourceCals_Company_ResourceGrpID_ResourceID_SpecialDay(Company, ResourceGrpID, ResourceID, SpecialDay, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ResourceCal for the service
   Description: Calls UpdateExt to update ResourceCal. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ResourceCal
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param SpecialDay: Desc: SpecialDay   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ResourceCalRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/ResourceCals(" + Company + "," + ResourceGrpID + "," + ResourceID + "," + SpecialDay + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ResourceCals_Company_ResourceGrpID_ResourceID_SpecialDay(Company, ResourceGrpID, ResourceID, SpecialDay, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ResourceCal item
   Description: Call UpdateExt to delete ResourceCal item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ResourceCal
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param SpecialDay: Desc: SpecialDay   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/ResourceCals(" + Company + "," + ResourceGrpID + "," + ResourceID + "," + SpecialDay + ")",headers=creds) as resp:
           return await resp.json()

async def get_EmpRoles(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EmpRoles items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EmpRoles
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpRoleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpRoles",headers=creds) as resp:
           return await resp.json()

async def post_EmpRoles(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EmpRoles
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EmpRoleRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EmpRoleRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpRoles", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EmpRoles_Company_EmpID_RoleCd(Company, EmpID, RoleCd, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EmpRole item
   Description: Calls GetByID to retrieve the EmpRole item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpRole
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param RoleCd: Desc: RoleCd   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpRoleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpRoles(" + Company + "," + EmpID + "," + RoleCd + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EmpRoles_Company_EmpID_RoleCd(Company, EmpID, RoleCd, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EmpRole for the service
   Description: Calls UpdateExt to update EmpRole. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EmpRole
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param RoleCd: Desc: RoleCd   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EmpRoleRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpRoles(" + Company + "," + EmpID + "," + RoleCd + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EmpRoles_Company_EmpID_RoleCd(Company, EmpID, RoleCd, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EmpRole item
   Description: Call UpdateExt to delete EmpRole item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EmpRole
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param RoleCd: Desc: RoleCd   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpRoles(" + Company + "," + EmpID + "," + RoleCd + ")",headers=creds) as resp:
           return await resp.json()

async def get_EntityGLCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EntityGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EntityGLCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EntityGLCs",headers=creds) as resp:
           return await resp.json()

async def post_EntityGLCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EntityGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EntityGLCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EntityGLC for the service
   Description: Calls UpdateExt to update EntityGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EntityGLC item
   Description: Call UpdateExt to delete EntityGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_EmpBasicAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EmpBasicAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EmpBasicAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpBasicAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasicAttches",headers=creds) as resp:
           return await resp.json()

async def post_EmpBasicAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EmpBasicAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EmpBasicAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EmpBasicAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasicAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EmpBasicAttches_Company_EmpID_DrawingSeq(Company, EmpID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EmpBasicAttch item
   Description: Calls GetByID to retrieve the EmpBasicAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpBasicAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpBasicAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasicAttches(" + Company + "," + EmpID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EmpBasicAttches_Company_EmpID_DrawingSeq(Company, EmpID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EmpBasicAttch for the service
   Description: Calls UpdateExt to update EmpBasicAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EmpBasicAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EmpBasicAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasicAttches(" + Company + "," + EmpID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EmpBasicAttches_Company_EmpID_DrawingSeq(Company, EmpID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EmpBasicAttch item
   Description: Call UpdateExt to delete EmpBasicAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EmpBasicAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasicAttches(" + Company + "," + EmpID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_Partners(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Partners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Partners
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartnerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/Partners",headers=creds) as resp:
           return await resp.json()

async def post_Partners(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Partners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartnerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartnerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/Partners", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Partners_Company_PartnerNum_PartnerType_PartnerID_SearchID(Company, PartnerNum, PartnerType, PartnerID, SearchID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Partner item
   Description: Calls GetByID to retrieve the Partner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Partner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartnerNum: Desc: PartnerNum   Required: True
      :param PartnerType: Desc: PartnerType   Required: True
      :param PartnerID: Desc: PartnerID   Required: True   Allow empty value : True
      :param SearchID: Desc: SearchID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartnerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/Partners(" + Company + "," + PartnerNum + "," + PartnerType + "," + PartnerID + "," + SearchID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Partners_Company_PartnerNum_PartnerType_PartnerID_SearchID(Company, PartnerNum, PartnerType, PartnerID, SearchID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Partner for the service
   Description: Calls UpdateExt to update Partner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Partner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartnerNum: Desc: PartnerNum   Required: True
      :param PartnerType: Desc: PartnerType   Required: True
      :param PartnerID: Desc: PartnerID   Required: True   Allow empty value : True
      :param SearchID: Desc: SearchID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartnerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/Partners(" + Company + "," + PartnerNum + "," + PartnerType + "," + PartnerID + "," + SearchID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Partners_Company_PartnerNum_PartnerType_PartnerID_SearchID(Company, PartnerNum, PartnerType, PartnerID, SearchID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Partner item
   Description: Call UpdateExt to delete Partner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Partner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartnerNum: Desc: PartnerNum   Required: True
      :param PartnerType: Desc: PartnerType   Required: True
      :param PartnerID: Desc: PartnerID   Required: True   Allow empty value : True
      :param SearchID: Desc: SearchID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/Partners(" + Company + "," + PartnerNum + "," + PartnerType + "," + PartnerID + "," + SearchID + ")",headers=creds) as resp:
           return await resp.json()

async def get_EmpRoleRts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EmpRoleRts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EmpRoleRts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpRoleRtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpRoleRts",headers=creds) as resp:
           return await resp.json()

async def post_EmpRoleRts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EmpRoleRts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EmpRoleRtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EmpRoleRtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpRoleRts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EmpRoleRts_Company_EmpID_RoleCd_Seq(Company, EmpID, RoleCd, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EmpRoleRt item
   Description: Calls GetByID to retrieve the EmpRoleRt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpRoleRt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param RoleCd: Desc: RoleCd   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpRoleRtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpRoleRts(" + Company + "," + EmpID + "," + RoleCd + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EmpRoleRts_Company_EmpID_RoleCd_Seq(Company, EmpID, RoleCd, Seq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EmpRoleRt for the service
   Description: Calls UpdateExt to update EmpRoleRt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EmpRoleRt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param RoleCd: Desc: RoleCd   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EmpRoleRtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpRoleRts(" + Company + "," + EmpID + "," + RoleCd + "," + Seq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EmpRoleRts_Company_EmpID_RoleCd_Seq(Company, EmpID, RoleCd, Seq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EmpRoleRt item
   Description: Call UpdateExt to delete EmpRoleRt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EmpRoleRt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param RoleCd: Desc: RoleCd   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpRoleRts(" + Company + "," + EmpID + "," + RoleCd + "," + Seq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpBasicListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseEmpBasic, whereClauseEmpBasicAttch, whereClauseEmpLabExpRate, whereClauseEmpCal, whereClausePartner, whereClauseResourceCal, whereClauseEmpRole, whereClauseEntityGLC, whereClauseEmpRoleRt, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "whereClauseEmpBasic=" + whereClauseEmpBasic
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseEmpBasicAttch=" + whereClauseEmpBasicAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseEmpLabExpRate=" + whereClauseEmpLabExpRate
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseEmpCal=" + whereClauseEmpCal
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePartner=" + whereClausePartner
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseResourceCal=" + whereClauseResourceCal
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseEmpRole=" + whereClauseEmpRole
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseEntityGLC=" + whereClauseEntityGLC
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseEmpRoleRt=" + whereClauseEmpRoleRt
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(empID, epicorHeaders = None):
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
   params += "empID=" + empID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetClientFileName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetClientFileName
   OperationID: GetClientFileName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetClientFileName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetClientFileName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Mins2Int(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Mins2Int
   OperationID: Mins2Int
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Mins2Int_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Mins2Int_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Hours2Int(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Hours2Int
   OperationID: Hours2Int
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Hours2Int_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Hours2Int_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Date2Int(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Date2Int
   OperationID: Date2Int
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Date2Int_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Date2Int_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckShift(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckShift
   Description: Check shift
   OperationID: CheckShift
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckShift_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckShift_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClockIn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ClockIn
   Description: Clock In
   OperationID: ClockIn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClockIn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClockIn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClockOut(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ClockOut
   Description: Clock Out
   OperationID: ClockOut
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClockOut_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClockOut_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CustomizeResourceCal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CustomizeResourceCal
   Description: This method will get a current ResourceCal record or create a temporary
ResourceCal record to be modified for a Employee.  The ProdHours will be
defaulted from the weekday of the selected date.  If any changes are made
to the ttResourceCal record, the UpdateResourceCal method will have to be
called to write the temporary ResourceCal record to the database.
   OperationID: CustomizeResourceCal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CustomizeResourceCal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustomizeResourceCal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeWFGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeWFGroup
   Description: Update the TaskSet fields according to the WF Group.
   OperationID: OnChangeWFGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeWFGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWFGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckClockInStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckClockInStatus
   Description: Called to check whether employee is clocked in and if so what shift they are clocked into.
   OperationID: CheckClockInStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckClockInStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckClockInStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByIDForTE(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIDForTE
   Description: Returns a DataSet given the primary key.  Contains special processing for
Time and Expense Entry.
   OperationID: GetByIDForTE
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDForTE_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDForTE_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByIDForTime(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIDForTime
   Description: Returns a DataSet given the primary key.  Contains special processing for
Time Entry.
   OperationID: GetByIDForTime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDForTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDForTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByIDForExpense(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIDForExpense
   Description: Returns a DataSet given the primary key.  Contains special processing for
Expense Entry.
   OperationID: GetByIDForExpense
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDForExpense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDForExpense_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultEmpID(epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultEmpID
   Description: Get Defaults Emp ID
   OperationID: GetDefaultEmpID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultEmpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetListExpEmployees(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListExpEmployees
   Description: Called to retrieve employees that can have expenses entered for them
   OperationID: GetListExpEmployees
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListExpEmployees_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListExpEmployees_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListForTE(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListForTE
   Description: Called to retrieve employees for Time and Expense Entry
   OperationID: GetListForTE
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListForTE_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForTE_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListForExpense(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListForExpense
   Description: Called to retrieve employees for Expense Entry
   OperationID: GetListForExpense
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListForExpense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForExpense_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListForTime(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListForTime
   Description: Called to retrieve employees for Time Entry
   OperationID: GetListForTime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListForTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPerConData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPerConData
   OperationID: GetPerConData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPerConData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPerConData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsFromList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsFromList
   Description: Get rows from list dataset
   OperationID: GetRowsFromList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsFromList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsFromList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsWhoIsNotHere(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsWhoIsNotHere
   Description: Calls the normal GetRows method and then screens out only those employees who should be here but are not.
   OperationID: GetRowsWhoIsNotHere
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsWhoIsNotHere_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsWhoIsNotHere_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCalendarID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCalendarID
   OperationID: OnChangeCalendarID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCalendarID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCalendarID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCurrencyCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCurrencyCode
   OperationID: OnChangeCurrencyCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeExpenseAllowed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeExpenseAllowed
   OperationID: OnChangeExpenseAllowed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeExpenseAllowed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeExpenseAllowed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeExpenseAutoApprove(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeExpenseAutoApprove
   OperationID: OnChangeExpenseAutoApprove
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeExpenseAutoApprove_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeExpenseAutoApprove_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeExpenseVendor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeExpenseVendor
   OperationID: OnChangeExpenseVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeExpenseVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeExpenseVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeRateEffectiveDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeRateEffectiveDate
   OperationID: OnChangeRateEffectiveDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeRateEffectiveDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRateEffectiveDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeRateEndDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeRateEndDate
   OperationID: OnChangeRateEndDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeRateEndDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRateEndDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeResource(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeResource
   OperationID: OnChangeResource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeResource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeResource_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeResourceGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeResourceGrp
   OperationID: OnChangeResourceGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeResourceGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeResourceGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeRoleCd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeRoleCd
   OperationID: OnChangeRoleCd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeRoleCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRoleCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTimeAutoApprove(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTimeAutoApprove
   OperationID: OnChangeTimeAutoApprove
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTimeAutoApprove_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTimeAutoApprove_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTimeTypeCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTimeTypeCode
   OperationID: OnChangeTimeTypeCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTimeTypeCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTimeTypeCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteCalendarException(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteCalendarException
   Description: This method will delete ResourceCal record.
   OperationID: DeleteCalendarException
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteCalendarException_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteCalendarException_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateResourceCal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateResourceCal
   Description: This method will check to see if the current ttResourceCal record was modified.
If it is a special working day or non-working day then it save the ttResourceCal
record to the database.
   OperationID: UpdateResourceCal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateResourceCal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateResourceCal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FromEffDateOverlaps(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FromEffDateOverlaps
   OperationID: FromEffDateOverlaps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FromEffDateOverlaps_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FromEffDateOverlaps_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetEmpStatusCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetEmpStatusCodeDescList
   OperationID: GetEmpStatusCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEmpStatusCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEmpStatusCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_getValidCompanyName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method getValidCompanyName
   OperationID: getValidCompanyName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getValidCompanyName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getValidCompanyName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetIfCurrentSiteHasExternalMES(epicorHeaders = None):
   """  
   Summary: Invoke method GetIfCurrentSiteHasExternalMES
   Description: Purpose:
Parameters:  none
Notes:
   OperationID: GetIfCurrentSiteHasExternalMES
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIfCurrentSiteHasExternalMES_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ModifySearchIDs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ModifySearchIDs
   Description: Modify Search ID.
   OperationID: ModifySearchIDs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ModifySearchIDs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ModifySearchIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEmpBasic(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEmpBasic
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEmpBasic
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEmpBasic_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmpBasic_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEmpBasicAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEmpBasicAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEmpBasicAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEmpBasicAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmpBasicAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEmpLabExpRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEmpLabExpRate
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEmpLabExpRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEmpLabExpRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmpLabExpRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEmpCal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEmpCal
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEmpCal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEmpCal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmpCal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewResourceCal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewResourceCal
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewResourceCal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewResourceCal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewResourceCal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEmpRole(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEmpRole
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEmpRole
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEmpRole_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmpRole_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEntityGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEntityGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEntityGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEntityGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEntityGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEmpRoleRt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEmpRoleRt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEmpRoleRt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEmpRoleRt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmpRoleRt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpBasicAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EmpBasicAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpBasicListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EmpBasicListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpBasicRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EmpBasicRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpCalRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EmpCalRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpLabExpRateRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EmpLabExpRateRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpRoleRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EmpRoleRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpRoleRtRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EmpRoleRtRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EntityGLCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartnerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartnerRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceCalRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ResourceCalRow] = obj["value"]
      pass

class Erp_Tablesets_EmpBasicAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.EmpID:str = obj["EmpID"]
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

class Erp_Tablesets_EmpBasicListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.FirstName:str = obj["FirstName"]
      """  First name of employee.  """  
      self.MiddleInitial:str = obj["MiddleInitial"]
      """  Middle name of employee.  """  
      self.LastName:str = obj["LastName"]
      """  Last name of employee  """  
      self.Name:str = obj["Name"]
      """  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.Phone:str = obj["Phone"]
      """  Home phone number  """  
      self.Shift:int = obj["Shift"]
      """  Normal work shift.  Value is to be defaulted from XASyst.DefaultShift (Production/Data Collection tab in Company Configuration) when available, otherwise it is not defaulted.  """  
      self.LaborRate:int = obj["LaborRate"]
      """  Labor rate that is used for Job Costing.  """  
      self.PRSetupReq:bool = obj["PRSetupReq"]
      """  An internally assigned flag that Indicates if the employee needs to be established in payroll. (Existence of PREmpMas). This flag is used to allow payroll employee maintenance view new employees created by job costing that were flagged as being "Payroll" employees.  """  
      self.EmpStatus:str = obj["EmpStatus"]
      """  Indicates the employment status. Can be A-Active, I-InActive or T-Terminated.  """  
      self.PhotoFile:str = obj["PhotoFile"]
      """  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  """  
      self.JCDept:str = obj["JCDept"]
      """   The Job Department in which the employee works work was done. An optional field. If entered must be valid in JCDept table.
Used by data collection in the "Work Que" window to provide a default department to view.  """  
      self.SupervisorID:str = obj["SupervisorID"]
      """   The ID of the Supervisor for the employee.  The Supervisor ID is actually the EmpID used for supervisor's PREmpMas record.
Validation: Can't be blank, if entered must be found in the PREmpMas file.  """  
      self.ServTech:bool = obj["ServTech"]
      """  This person usually goes out on service calls  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """   Links the employee to a UserID.  This link is used by the Shop Floor Menu(SFM).  In the SFM, the user signs on with their employee id instead of a User id. This link grants the menu security authorizations of the User to the employee. It also defines the language to be used.
Note: An employee can only be related to one UserFile record. Each UserFile, can be related to many employees.  Therefore, you might set up a few generic Users per language, or based on security levels or you might set up a user for each employee. Note: Many transactions, are stamped with the UserID, thus if you use generic users you will be tracking to the individual employee.
This field is OPTIONAL. However, employee will not be allowed to login to the SFM without a being linked to a UserID.  Also, the company of the employee must be an authorized company of the user. This is validated by the finding a record in UserComp table, using EmpBasic.Company, EmpBasic.DCDUserID.  """  
      self.ShopSupervisor:bool = obj["ShopSupervisor"]
      """  Indicates if this employee is a shop supervisor. This must be checked for employee to use the Shop Floor Menu Supervisor options.  """  
      self.WarehouseManager:bool = obj["WarehouseManager"]
      """  A warehouse manager has the access to the Manager's Queue tab in the Material Request Queue.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Resource Group ID for this employee, only allowed if the Project Billing module licensed.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Resource D for this employee, only allowed if the Project Billing module licensed.  """  
      self.SupervisorName:str = obj["SupervisorName"]
      """  SupervisorName  """  
      self.ShiftDescription:str = obj["ShiftDescription"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ResourceGroupDescription:str = obj["ResourceGroupDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EmpBasicRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.FirstName:str = obj["FirstName"]
      """  First name of employee.  """  
      self.MiddleInitial:str = obj["MiddleInitial"]
      """  Middle name of employee.  """  
      self.LastName:str = obj["LastName"]
      """  Last name of employee  """  
      self.Name:str = obj["Name"]
      """  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.Address:str = obj["Address"]
      """  First Address Line  """  
      self.Address2:str = obj["Address2"]
      """  Second Address Line  """  
      self.City:str = obj["City"]
      """  City portion of address  """  
      self.State:str = obj["State"]
      """  Home State. Can be blank.  """  
      self.ZIP:str = obj["ZIP"]
      """  Postal Code or Zip code portion of address  """  
      self.Country:str = obj["Country"]
      """  Country is used as part of the mailing address. It can be left blank.  """  
      self.Phone:str = obj["Phone"]
      """  Home phone number  """  
      self.EmgPhone:str = obj["EmgPhone"]
      """  Emergency Phone number  """  
      self.Shift:int = obj["Shift"]
      """  Normal work shift.  Value is to be defaulted from XASyst.DefaultShift (Production/Data Collection tab in Company Configuration) when available, otherwise it is not defaulted.  """  
      self.LaborRate:int = obj["LaborRate"]
      """  Labor rate that is used for Job Costing.  """  
      self.Payroll:bool = obj["Payroll"]
      """   Indicates if this employee is should be paid through the Manufacturing System payroll module.  This does not mean they have been setup in payroll, only that they should be.
Once setup in payroll (existence of corresponding PREmpMas record) this field cannot be changed.  """  
      self.PRSetupReq:bool = obj["PRSetupReq"]
      """  An internally assigned flag that Indicates if the employee needs to be established in payroll. (Existence of PREmpMas). This flag is used to allow payroll employee maintenance view new employees created by job costing that were flagged as being "Payroll" employees.  """  
      self.EmpStatus:str = obj["EmpStatus"]
      """  Indicates the employment status. Can be A-Active, I-InActive or T-Terminated.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """   The default expense code that will be for direct labor hours reported by this employee.  This must be valid in the LabExpCd master file.
This will be used unless labor is reported where the JobHead.ExpenseCode is not blank.  """  
      self.PhotoFile:str = obj["PhotoFile"]
      """  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  """  
      self.JCDept:str = obj["JCDept"]
      """   The Job Department in which the employee works work was done. An optional field. If entered must be valid in JCDept table.
Used by data collection in the "Work Que" window to provide a default department to view.  """  
      self.EmgContact:str = obj["EmgContact"]
      """  Emergency contact name.  """  
      self.SupervisorID:str = obj["SupervisorID"]
      """   The ID of the Supervisor for the employee.  The Supervisor ID is actually the EmpID used for supervisor's PREmpMas record.
Validation: Can't be blank, if entered must be found in the PREmpMas file.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.ServTech:bool = obj["ServTech"]
      """  This person usually goes out on service calls  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Email address of the Employee.  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """   Links the employee to a UserID.  This link is used by the Shop Floor Menu(SFM).  In the SFM, the user signs on with their employee id instead of a User id. This link grants the menu security authorizations of the User to the employee. It also defines the language to be used.
Note: An employee can only be related to one UserFile record. Each UserFile, can be related to many employees.  Therefore, you might set up a few generic Users per language, or based on security levels or you might set up a user for each employee. Note: Many transactions, are stamped with the UserID, thus if you use generic users you will be tracking to the individual employee.
This field is OPTIONAL. However, employee will not be allowed to login to the SFM without a being linked to a UserID.  Also, the company of the employee must be an authorized company of the user. This is validated by the finding a record in UserComp table, using EmpBasic.Company, EmpBasic.DCDUserID.  """  
      self.ProductionWorker:bool = obj["ProductionWorker"]
      """  Indicates if this employee works on the manufacturing line. This must be checked for employee to use the Shop Floor Menu production options.  """  
      self.MaterialHandler:bool = obj["MaterialHandler"]
      """  Indicates if this employee is a material handler. This must be checked for employee to use the Shop Floor Menu material handler options.  """  
      self.ShopSupervisor:bool = obj["ShopSupervisor"]
      """  Indicates if this employee is a shop supervisor. This must be checked for employee to use the Shop Floor Menu Supervisor options.  """  
      self.CanReportQty:bool = obj["CanReportQty"]
      """   Pertains to Data Collection only.
Indicates if the employee is allowed report completed quantities.  """  
      self.CanOverrideJob:bool = obj["CanOverrideJob"]
      """   Pertains to Data Collection only.
Indicates if the job/asm/opr can be overriden when reporting completed quantity.  If NO, then they will only be allowed to report against a job/asm/opr that they are currently working on (active labordtl record ) or where the job is open and the operation is marked as "quantity only" reporting .  If YES, they can enter the quantity for any open job without first having to do a start activity function.
( See also EmpBasic.CanReportQty )  """  
      self.CanRequestMaterial:bool = obj["CanRequestMaterial"]
      """   Pertains to Data Collection/Advanced Material Management only.
Indicates if the employee is allowed make requests for materials.  """  
      self.CanReportScrapQty:bool = obj["CanReportScrapQty"]
      """   Pertains to Data Collection only.
Indicates if the employee is allowed report scrap quantities.  """  
      self.CanReportNCQty:bool = obj["CanReportNCQty"]
      """   Pertains to Data Collection only.
Indicates if the employee is allowed report nonconformance quantities.  """  
      self.ShipRecv:bool = obj["ShipRecv"]
      """  Indicates if this employee is a Shipping/Receiving worker. This must be checked for employee to use the Shop Floor Menu Shipping/Receiving options.  """  
      self.CnvEmpID:str = obj["CnvEmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.WarehouseManager:bool = obj["WarehouseManager"]
      """  A warehouse manager has the access to the Manager's Queue tab in the Material Request Queue.  """  
      self.CanOverrideAllocations:bool = obj["CanOverrideAllocations"]
      """  Employee is able to override a hard allocation against inventory and select it from another Bin during the process of picking and packing orders, as long as it is not allocated to another Sales Order, Job or Transfer Order.  """  
      self.AllowDirLbr:bool = obj["AllowDirLbr"]
      """  If false the shop employee will not be allowed to book time to manufacturing jobs.  """  
      self.ContractEmp:bool = obj["ContractEmp"]
      """  True indicates that the shop employee is on contract rather than paid via the payroll. This flag is then used in the advanced billing invoice preparation process.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Resource Group ID for this employee, only allowed if the Project Billing module licensed.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Resource D for this employee, only allowed if the Project Billing module licensed.  """  
      self.TimeWFGroupID:str = obj["TimeWFGroupID"]
      """  Unique identifier of the workflow group for this employee's Time transactions.  """  
      self.ExpenseEntryAllowed:bool = obj["ExpenseEntryAllowed"]
      """  This value will be true if the Employee is allowed to enter Expense.  """  
      self.ExpenseWFGroupID:str = obj["ExpenseWFGroupID"]
      """  Unique identifier of the workflow group for this employee's Expense transactions.  """  
      self.ExpenseVendorNum:int = obj["ExpenseVendorNum"]
      """  The Supplier Number associated to the Employee for Expense entry.  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.SyncNameToPerCon:bool = obj["SyncNameToPerCon"]
      """  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  """  
      self.SyncAddressToPerCon:bool = obj["SyncAddressToPerCon"]
      """  Default to True. If unchecked then changes to the Address fields on PerCon won't affect this record and visa versa.  """  
      self.SyncPhoneToPerCon:bool = obj["SyncPhoneToPerCon"]
      """  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  """  
      self.SyncEmailToPerCon:bool = obj["SyncEmailToPerCon"]
      """  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  """  
      self.CanEnterIndirectTime:bool = obj["CanEnterIndirectTime"]
      """   Pertains to Time Management.
Maintains whether the employee is allowed to enter Indirect time.  """  
      self.CanEnterProductionTime:bool = obj["CanEnterProductionTime"]
      """   Pertains to Time Management.
Maintains whether the employee is allowed to enter Production time.  """  
      self.CanEnterProjectTime:bool = obj["CanEnterProjectTime"]
      """   Pertains to Time Management.
Maintains whether the employee is allowed to enter Project time.  """  
      self.CanEnterServiceTime:bool = obj["CanEnterServiceTime"]
      """   Pertains to Time Management.
Maintains whether the employee is allowed to enter Service time.  """  
      self.CanEnterSetupTime:bool = obj["CanEnterSetupTime"]
      """   Pertains to Time Management.
Maintains whether the employee is allowed to enter Setup time.  """  
      self.TimeAutoApprove:bool = obj["TimeAutoApprove"]
      """  Time transactions for the employee requiring employee approval logic will automatically be approved.  """  
      self.ExpenseAutoApprove:bool = obj["ExpenseAutoApprove"]
      """  Expense transactions for the employee requiring employee approval logic will automatically be approved.  """  
      self.MobileUserPassword:str = obj["MobileUserPassword"]
      """  Mobile Password  """  
      self.AllowIndirect:bool = obj["AllowIndirect"]
      """  Default is True.  Determines if an employee can enter time with a labor type of Indirect.  If True, an employee may select Indirect labor type.  If false, employee may not select Indirect labor type in Time Entry.  """  
      self.AllowProduction:bool = obj["AllowProduction"]
      """  Default is True.  Determines if an employee can enter time with a labor type of Production.  If True, an employee may select Production labor type.  If false, employee may not select Production labor type in Time Entry.  """  
      self.AllowProject:bool = obj["AllowProject"]
      """  Default is True.  Determines if an employee can enter time with a labor type of Project.  If True, an employee may select Project labor type.  If false, employee may not select Project labor type in Time Entry.  """  
      self.AllowService:bool = obj["AllowService"]
      """  Default is True.  Determines if an employee can enter time with a labor type of Service.  If True, an employee may select Service labor type.  If false, employee may not select Service labor type in Time Entry.  """  
      self.AllowSetup:bool = obj["AllowSetup"]
      """  Default is True.  Determines if an employee can enter time with a labor type of Setup.  If True, an employee may select Setup labor type.  If false, employee may not select Setup labor type in Time Entry.  """  
      self.DefaultLaborTypePseudo:str = obj["DefaultLaborTypePseudo"]
      """   Correlates to LaborType.  Indicates the type of labor transaction, however "Production" LaborType can be broken out into "Project", "Production" or "Service".  Valid Values are "I" = Indirect, "P" - Production, "S" - Setup, "J" - Project, or "V" - Service.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  """  
      self.DefaultTimeTypCd:str = obj["DefaultTimeTypCd"]
      """  Time Type Code  """  
      self.DefaultIndirectCode:str = obj["DefaultIndirectCode"]
      """  A code that links to the Indirect master record that describes the type of indirect labor for this transaction. This field IS DIRECTLY ENTERED, not via a description/selection list method.   This is only valid when LaborType = "I" and must then be valid.  """  
      self.DefaultExpenseCode:str = obj["DefaultExpenseCode"]
      """  The expense code for this labor transaction. An expense code is a abbreviated method of indirectly assigning a G/L account for the labor expense. DEFAULTS: for direct labor;  use the JobHead.ExpenseCode if its non-blank,  else use the Employee.ExpenseCode.                                                                   For Indirect Labor use the Indirect.ExpenseCode if not blank, else use the employee.ExpenseCode.  """  
      self.DefaultResourceGrpID:str = obj["DefaultResourceGrpID"]
      """   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group table.
For production labor (LaborType = "S" or "P") the default is from the JobOper.PrimaryProdDtl JobOpDtl.ResourceGrpID.
For indirect labor (LaborType = I) there is no default.  """  
      self.DefaultResourceID:str = obj["DefaultResourceID"]
      """  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  """  
      self.DefaultLaborHrs:int = obj["DefaultLaborHrs"]
      """  Labor hours are used in calculating labor cost for a job. It is stored as hours-hundredths. It is calculated whenever the start/stop time is changed. It can then be overridden.  """  
      self.DefaultExpCurrencyCode:str = obj["DefaultExpCurrencyCode"]
      """  The currency the expense occurred in.  """  
      self.DefaultClaimCurrencyCode:str = obj["DefaultClaimCurrencyCode"]
      """  The currency the claim amounts are in.  """  
      self.DefaultPMUID:int = obj["DefaultPMUID"]
      """  The payment method of the expense.  """  
      self.DefaultTaxRegionCode:str = obj["DefaultTaxRegionCode"]
      """  The Tax Region for this expense.  """  
      self.DefaultTaxIncluded:bool = obj["DefaultTaxIncluded"]
      """  Indicates if the expense amount includes tax.  """  
      self.ExpenseAdvReqAllowed:bool = obj["ExpenseAdvReqAllowed"]
      """  This value will be true if the Employee is allowed to enter Expense for advance requests.  """  
      self.ExpenseAdvReqWFGroupID:str = obj["ExpenseAdvReqWFGroupID"]
      """  Unique identifier of the workflow group for this employee's Expense advance request transactions.  """  
      self.ExpenseAdvReqAutoApprove:bool = obj["ExpenseAdvReqAutoApprove"]
      """  Advance request expense transactions for the employee requiring employee approval logic will automatically be approved.  """  
      self.MobileResourceID:str = obj["MobileResourceID"]
      """  MobileResourceID  """  
      self.AllowAsAltRemitTo:bool = obj["AllowAsAltRemitTo"]
      """  AllowAsAltRemitTo  """  
      self.UserNameInJDF:str = obj["UserNameInJDF"]
      """  UserNameInJDF  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.PermitScrap:bool = obj["PermitScrap"]
      """  PermitScrap  """  
      self.PermitDown:bool = obj["PermitDown"]
      """  PermitDown  """  
      self.PermitHelp:bool = obj["PermitHelp"]
      """  PermitHelp  """  
      self.PermitJobControl:bool = obj["PermitJobControl"]
      """  PermitJobControl  """  
      self.PermitNextJobControl:bool = obj["PermitNextJobControl"]
      """  PermitNextJobControl  """  
      self.PermitManualSqc:bool = obj["PermitManualSqc"]
      """  PermitManualSqc  """  
      self.PermitVariableSqc:bool = obj["PermitVariableSqc"]
      """  PermitVariableSqc  """  
      self.PermitAttributeSqc:bool = obj["PermitAttributeSqc"]
      """  PermitAttributeSqc  """  
      self.PermitMaterialLot:bool = obj["PermitMaterialLot"]
      """  PermitMaterialLot  """  
      self.PermitSetupMaterial:bool = obj["PermitSetupMaterial"]
      """  PermitSetupMaterial  """  
      self.PermitCavities:bool = obj["PermitCavities"]
      """  PermitCavities  """  
      self.PermitPercentRegrind:bool = obj["PermitPercentRegrind"]
      """  PermitPercentRegrind  """  
      self.PermitSaveProfile:bool = obj["PermitSaveProfile"]
      """  PermitSaveProfile  """  
      self.PermitCalibration:bool = obj["PermitCalibration"]
      """  PermitCalibration  """  
      self.PermitMachinePm:bool = obj["PermitMachinePm"]
      """  PermitMachinePm  """  
      self.PermitToolPm:bool = obj["PermitToolPm"]
      """  PermitToolPm  """  
      self.PermitLanguage:bool = obj["PermitLanguage"]
      """  PermitLanguage  """  
      self.PermitPreferences:bool = obj["PermitPreferences"]
      """  PermitPreferences  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DisallowTimeEntry:bool = obj["DisallowTimeEntry"]
      """  The purpose of the flag is to disallow an employee to enter their own time in Time and Expense Entry  """  
      self.PkgInboundAllowed:bool = obj["PkgInboundAllowed"]
      """  Indicates that an employee can execute inbound related transactions on the shop floor. The default for the check box is unchecked.  """  
      self.PkgOutboundAllowed:bool = obj["PkgOutboundAllowed"]
      """  Indicates that an employee can execute outbound related transactions on the shop floor. The default for the check box is unchecked.  """  
      self.PkgInventoryAllowed:bool = obj["PkgInventoryAllowed"]
      """  Indicates that an employee can execute inventory related transactions on the shop floor. The default for the check box is unchecked.  """  
      self.PkgManufacturingAllowed:bool = obj["PkgManufacturingAllowed"]
      """  Indicates that an employee can execute manufacturing related transactions on the shop floor. The default for the check box is unchecked.  """  
      self.PkgQualityAllowed:bool = obj["PkgQualityAllowed"]
      """  Indicates that an employee can execute quality related transactions on the shop floor. The default for the check box is unchecked.  """  
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.PkgMasterMixedPrint:bool = obj["PkgMasterMixedPrint"]
      """  Package Control Activity setting to indicate if the employee is allowed to print during the Master and MixedMaster.  """  
      self.PkgSuppressPrintMessages:bool = obj["PkgSuppressPrintMessages"]
      """  PkgSuppressPrintMessages  """  
      self.PayrollValuesForHCM:str = obj["PayrollValuesForHCM"]
      """  PayrollValuesForHCM  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the employee has to be synchronized with Epicor FSA application.  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.IDDocument:str = obj["IDDocument"]
      """  Identity Document  """  
      self.BirthDate:str = obj["BirthDate"]
      """  Birthdate  """  
      self.Sex:str = obj["Sex"]
      """  Sex  """  
      self.Department:str = obj["Department"]
      """  Department  """  
      self.EnrollmentDate:str = obj["EnrollmentDate"]
      """  Enrollment Date  """  
      self.DepartureDate:str = obj["DepartureDate"]
      """  Departure Date  """  
      self.AlertFlag:bool = obj["AlertFlag"]
      """  Should this employee receive email alert messages.  """  
      self.DepartmentDescription:str = obj["DepartmentDescription"]
      """  Department Description  """  
      self.EnableExpenseSupplier:bool = obj["EnableExpenseSupplier"]
      """  external field for UI to use to know whether it should enable or disable the ExpenseVendorNumVendorID field.  """  
      self.ExpenseDescription:str = obj["ExpenseDescription"]
      """  Expense Description  """  
      self.ExpenseDisableCreate:bool = obj["ExpenseDisableCreate"]
      """  Indicates whether the user is allowed to create Expense transactions in Time and Expense Entry for another employee for which they are an Approver.  """  
      self.ExpenseRestrictEntry:bool = obj["ExpenseRestrictEntry"]
      self.FoundPayroll:bool = obj["FoundPayroll"]
      """  Payroll record has been found so changes to many fields are disallowed.  """  
      self.FoundPayrollUserAllowed:bool = obj["FoundPayrollUserAllowed"]
      """  Payroll record has been found so changes to many fields are disallowed, but the user is in the employee's payroll class so can see the labor rate field  """  
      self.HCMEnabledAt:str = obj["HCMEnabledAt"]
      """  String value which contains the validations for the HCM Integration, possible values NON(Nothing configured), HDR (Header) DTL (Detail)  """  
      self.IsHCMAllowedByEmp:bool = obj["IsHCMAllowedByEmp"]
      """  External field used on Employee Entry in order to enable/disable HCM configuration  """  
      self.PayrollValuesForHCMDsp:str = obj["PayrollValuesForHCMDsp"]
      """  Displays blank if "Allow Override Integrate Labor Pay Hours at Employee" checkbox in Site configuration is unchecked and Employee's value if checked.  """  
      self.PerConName:str = obj["PerConName"]
      self.PhotoFilePath:str = obj["PhotoFilePath"]
      """  Path to the photo file if it exists.  """  
      self.SetShopLoad:bool = obj["SetShopLoad"]
      """  Flag used to indicate that the generate fill shop capacity process needs to be run to update the ShopCap records because new records won't be added due performance.  """  
      self.ShiftEndTime:str = obj["ShiftEndTime"]
      """  Shift end time in Hours:Minute format., used by Shop Tracker  """  
      self.ShiftStartTime:str = obj["ShiftStartTime"]
      """  Shift start time in Hours:Minutes format  """  
      self.SupervisorName:str = obj["SupervisorName"]
      """  SupervisorName  """  
      self.TimeDisableCreate:bool = obj["TimeDisableCreate"]
      """  Indicates whether the user is allowed to create a Time transaction in Time and Expense Entry for another employee for which they are an Approver.  """  
      self.TimeRestrictEntry:bool = obj["TimeRestrictEntry"]
      self.UserIDName:str = obj["UserIDName"]
      """  User ID Name  """  
      self.CalendarID:str = obj["CalendarID"]
      self.COASegReferences:str = obj["COASegReferences"]
      """  List of fields which are referenced by COA segments.  """  
      self.TimeApprovalTasksTree:str = obj["TimeApprovalTasksTree"]
      """  This column used to display Time Approval Task tree in MetaUI  """  
      self.ExpenseApprovalTasksTree:str = obj["ExpenseApprovalTasksTree"]
      """  This column used to display Time Approval Task tree in MetaUI  """  
      self.ShiftLength:int = obj["ShiftLength"]
      self.BitFlag:int = obj["BitFlag"]
      self.CompanySendToFSA:bool = obj["CompanySendToFSA"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.ExpenseCodeDescription:str = obj["ExpenseCodeDescription"]
      self.ExpenseVendorNumName:str = obj["ExpenseVendorNumName"]
      self.ExpenseVendorNumCity:str = obj["ExpenseVendorNumCity"]
      self.ExpenseVendorNumTermsCode:str = obj["ExpenseVendorNumTermsCode"]
      self.ExpenseVendorNumAddress3:str = obj["ExpenseVendorNumAddress3"]
      self.ExpenseVendorNumDefaultFOB:str = obj["ExpenseVendorNumDefaultFOB"]
      self.ExpenseVendorNumCurrencyCode:str = obj["ExpenseVendorNumCurrencyCode"]
      self.ExpenseVendorNumZIP:str = obj["ExpenseVendorNumZIP"]
      self.ExpenseVendorNumVendorID:str = obj["ExpenseVendorNumVendorID"]
      self.ExpenseVendorNumAddress2:str = obj["ExpenseVendorNumAddress2"]
      self.ExpenseVendorNumAddress1:str = obj["ExpenseVendorNumAddress1"]
      self.ExpenseVendorNumCountry:str = obj["ExpenseVendorNumCountry"]
      self.ExpenseVendorNumState:str = obj["ExpenseVendorNumState"]
      self.JCDeptDescription:str = obj["JCDeptDescription"]
      self.MachineDescription:str = obj["MachineDescription"]
      self.ResourceDescription:str = obj["ResourceDescription"]
      self.ResourceGroupDescription:str = obj["ResourceGroupDescription"]
      self.ShiftDescription:str = obj["ShiftDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EmpCalRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.CalendarID:str = obj["CalendarID"]
      """  Epmloyee Calendar ID  """  
      self.FromEffectiveDate:str = obj["FromEffectiveDate"]
      """  From Effective Date of this Calendar for this Employee.  The value must be unique per Company/Employee/Calendar.  This value cannot be changed after the initial save.  """  
      self.ToEffectiveDate:str = obj["ToEffectiveDate"]
      """  To Effective Date of this Calendar for this Employee.  Value is not required.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CalendarIDDescription:str = obj["CalendarIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EmpLabExpRateRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.EmpID:str = obj["EmpID"]
      """  EmpID  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode  """  
      self.RateType:int = obj["RateType"]
      """  RateType  """  
      self.RateMultiplier:int = obj["RateMultiplier"]
      """  RateMultiplier  """  
      self.FixedRate:int = obj["FixedRate"]
      """  FixedRate  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.EmpBasicName:str = obj["EmpBasicName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EmpRoleRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RoleCd:str = obj["RoleCd"]
      """  Project Role Code  """  
      self.Primary:bool = obj["Primary"]
      """  Setting this to true defines this role code as the  primary Project Role for the employee.ONLY one role code can be defined as primary.  """  
      self.TimeApprover:bool = obj["TimeApprover"]
      """  Determines if this Employee is a Time Approver through this Role.  """  
      self.ExpenseApprover:bool = obj["ExpenseApprover"]
      """  Determines if this Employee is a Expense Approver through this Role.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.EmpBasicName:str = obj["EmpBasicName"]
      self.EmpBasicFirstName:str = obj["EmpBasicFirstName"]
      self.EmpBasicLastName:str = obj["EmpBasicLastName"]
      self.RoleCdRoleDescription:str = obj["RoleCdRoleDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EmpRoleRtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RoleCd:str = obj["RoleCd"]
      """  Project Role Code  """  
      self.RateEffDte:str = obj["RateEffDte"]
      """  The effective date of the project role code rate.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.TimeTypCd:str = obj["TimeTypCd"]
      """  Time Type Code  """  
      self.Rate:int = obj["Rate"]
      """  The charge rate for project role code expressed in the designated currency code.  """  
      self.RateEndDte:str = obj["RateEndDte"]
      """  The end date of the project role code rate.  """  
      self.Seq:int = obj["Seq"]
      """  Sequence field used to keep the primary key unique  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.EmpBasicFirstName:str = obj["EmpBasicFirstName"]
      self.EmpBasicName:str = obj["EmpBasicName"]
      self.EmpBasicLastName:str = obj["EmpBasicLastName"]
      self.RoleCdRoleDescription:str = obj["RoleCdRoleDescription"]
      self.TimeTypCdDescription:str = obj["TimeTypCdDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Identifier of the GL Control Type.  """  
      self.GLControlCode:str = obj["GLControlCode"]
      """  GL Control Identifier.  """  
      self.BusinessEntity:str = obj["BusinessEntity"]
      """  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.GlobalEntityGLC:bool = obj["GlobalEntityGLC"]
      """  Marks this EntityGLC as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the related BankAcct record.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      self.CallCode:str = obj["CallCode"]
      """  CallCode of the related FSCallCd record.  """  
      self.ChargeCode:str = obj["ChargeCode"]
      self.ClassCode:str = obj["ClassCode"]
      """  ClassCode of the related FAClass record.  """  
      self.ClassID:str = obj["ClassID"]
      """  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  """  
      self.ContractCode:str = obj["ContractCode"]
      """  ContractCode of the related FSContCd record.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode of the related Currency record.  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum of the related Customer record  """  
      self.DeductionID:str = obj["DeductionID"]
      """  DeductionID of PRClsDed or PRDeduct.  """  
      self.EmpID:str = obj["EmpID"]
      """  EmpID of the related PREmpMas record.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode of PayTLbr, LabExpCd  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID of ExtCompany table  """  
      self.FromPlant:str = obj["FromPlant"]
      """  FromPlant value of the related PlntTranDef record.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  GroupCode of the related FAGroup record.  """  
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.JCDept:str = obj["JCDept"]
      """  JCDept of the related JCDept record.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  MiscCode of the related MiscChrg or PurMisc record.  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum of the related Part record.  """  
      self.PayTypeID:str = obj["PayTypeID"]
      """  PayTypeID of PayType  """  
      self.PerConName:str = obj["PerConName"]
      self.PIStatus:str = obj["PIStatus"]
      """  PI Status  """  
      self.Plant:str = obj["Plant"]
      """  Plant of the related PlantConfCtrl record.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdCode of the related ProdGrup record.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID of the related Project record.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  PurchCode of the related GLPurch record.  """  
      self.RateCode:str = obj["RateCode"]
      """  RateCode of the related GLRate record.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  ReasonCode of the related Reason record.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  ReasonType of the related Reason record.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  SalesCatID of the related SalesCat record.  """  
      self.Shift:int = obj["Shift"]
      """  Shift value of the related JCShift record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode of the related SalesTax record.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  TaxTblID of PRTaxMas or PRClsTax.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  ToPlant value of the related PlntTranDef record.  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  TransferMethod of ExtCompany table  """  
      self.TypeID:str = obj["TypeID"]
      """  Type ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum of the related Vendor record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  WarehouseCode of the related Warehse record.  """  
      self.ExpenseTypeCode:str = obj["ExpenseTypeCode"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.OprTypeCode:str = obj["OprTypeCode"]
      self.CashDeskID:str = obj["CashDeskID"]
      self.TIN:str = obj["TIN"]
      self.ReclassCodeID:str = obj["ReclassCodeID"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartnerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PartnerNum:int = obj["PartnerNum"]
      """  PartnerNum  """  
      self.PartnerType:int = obj["PartnerType"]
      """  PartnerType  """  
      self.SearchID:str = obj["SearchID"]
      """  SearchID  """  
      self.IsActive:bool = obj["IsActive"]
      """  IsActive  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.PartnerID:str = obj["PartnerID"]
      """  PartnerID  """  
      self.DspSearchID:str = obj["DspSearchID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ResourceCalRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  A code uniquely identifies a Resource Group.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource.  """  
      self.SpecialDay:str = obj["SpecialDay"]
      """  Exception Day  """  
      self.ProdHour01:bool = obj["ProdHour01"]
      """  ProdHour01  """  
      self.ProdHour02:bool = obj["ProdHour02"]
      """  ProdHour02  """  
      self.ProdHour03:bool = obj["ProdHour03"]
      """  ProdHour03  """  
      self.ProdHour04:bool = obj["ProdHour04"]
      """  ProdHour04  """  
      self.ProdHour05:bool = obj["ProdHour05"]
      """  ProdHour05  """  
      self.ProdHour06:bool = obj["ProdHour06"]
      """  ProdHour06  """  
      self.ProdHour07:bool = obj["ProdHour07"]
      """  ProdHour07  """  
      self.ProdHour08:bool = obj["ProdHour08"]
      """  ProdHour08  """  
      self.ProdHour09:bool = obj["ProdHour09"]
      """  ProdHour09  """  
      self.ProdHour10:bool = obj["ProdHour10"]
      """  ProdHour10  """  
      self.ProdHour11:bool = obj["ProdHour11"]
      """  ProdHour11  """  
      self.ProdHour12:bool = obj["ProdHour12"]
      """  ProdHour12  """  
      self.ProdHour13:bool = obj["ProdHour13"]
      """  ProdHour13  """  
      self.ProdHour14:bool = obj["ProdHour14"]
      """  ProdHour14  """  
      self.ProdHour15:bool = obj["ProdHour15"]
      """  ProdHour15  """  
      self.ProdHour16:bool = obj["ProdHour16"]
      """  ProdHour16  """  
      self.ProdHour17:bool = obj["ProdHour17"]
      """  ProdHour17  """  
      self.ProdHour18:bool = obj["ProdHour18"]
      """  ProdHour18  """  
      self.ProdHour19:bool = obj["ProdHour19"]
      """  ProdHour19  """  
      self.ProdHour20:bool = obj["ProdHour20"]
      """  ProdHour20  """  
      self.ProdHour21:bool = obj["ProdHour21"]
      """  ProdHour21  """  
      self.ProdHour22:bool = obj["ProdHour22"]
      """  ProdHour22  """  
      self.ProdHour23:bool = obj["ProdHour23"]
      """  ProdHour23  """  
      self.ProdHour24:bool = obj["ProdHour24"]
      """  ProdHour24  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExceptionLabel:str = obj["ExceptionLabel"]
      """  ExceptionLabel  """  
      self.DispExceptionLabel:str = obj["DispExceptionLabel"]
      """  Display Exception Label  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckClockInStatus_input:
   """ Required : 
   empID
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      """  Employee ID  """  
      pass

class CheckClockInStatus_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EmpBasicTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.clockIn:bool = obj["clockIn"]
      self.shift:int = obj["parameters"]
      self.downtime:bool = obj["downtime"]
      self.clockInTimeStr:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckShift_input:
   """ Required : 
   ipEmpID
   ipLaborShift
   """  
   def __init__(self, obj):
      self.ipEmpID:str = obj["ipEmpID"]
      """  Employee ID  """  
      self.ipLaborShift:int = obj["ipLaborShift"]
      """  Labor Shift  """  
      pass

class CheckShift_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ClockIn_input:
   """ Required : 
   employeeID
   shift
   """  
   def __init__(self, obj):
      self.employeeID:str = obj["employeeID"]
      """  Employee ID  """  
      self.shift:int = obj["shift"]
      """  Labor Shift  """  
      pass

class ClockIn_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Clock in time and date as a formatted string  """  
      pass

class ClockOut_input:
   """ Required : 
   employeeID
   """  
   def __init__(self, obj):
      self.employeeID:str = obj["employeeID"]
      """  Employee ID  """  
      pass

class ClockOut_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.employeeID:str = obj["parameters"]
      pass

      """  output parameters  """  

class CustomizeResourceCal_input:
   """ Required : 
   ipEmpID
   ipDate
   ds
   """  
   def __init__(self, obj):
      self.ipEmpID:str = obj["ipEmpID"]
      """  The current Employee ID  """  
      self.ipDate:str = obj["ipDate"]
      """  The selected date to be customized  """  
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

class CustomizeResourceCal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Date2Int_input:
   """ Required : 
   vBegTime
   vEndTime
   vDate
   """  
   def __init__(self, obj):
      self.vBegTime:str = obj["vBegTime"]
      self.vEndTime:str = obj["vEndTime"]
      self.vDate:str = obj["vDate"]
      pass

class Date2Int_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   empID
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteCalendarException_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

class DeleteCalendarException_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_EmpBasicAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.EmpID:str = obj["EmpID"]
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

class Erp_Tablesets_EmpBasicListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.FirstName:str = obj["FirstName"]
      """  First name of employee.  """  
      self.MiddleInitial:str = obj["MiddleInitial"]
      """  Middle name of employee.  """  
      self.LastName:str = obj["LastName"]
      """  Last name of employee  """  
      self.Name:str = obj["Name"]
      """  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.Phone:str = obj["Phone"]
      """  Home phone number  """  
      self.Shift:int = obj["Shift"]
      """  Normal work shift.  Value is to be defaulted from XASyst.DefaultShift (Production/Data Collection tab in Company Configuration) when available, otherwise it is not defaulted.  """  
      self.LaborRate:int = obj["LaborRate"]
      """  Labor rate that is used for Job Costing.  """  
      self.PRSetupReq:bool = obj["PRSetupReq"]
      """  An internally assigned flag that Indicates if the employee needs to be established in payroll. (Existence of PREmpMas). This flag is used to allow payroll employee maintenance view new employees created by job costing that were flagged as being "Payroll" employees.  """  
      self.EmpStatus:str = obj["EmpStatus"]
      """  Indicates the employment status. Can be A-Active, I-InActive or T-Terminated.  """  
      self.PhotoFile:str = obj["PhotoFile"]
      """  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  """  
      self.JCDept:str = obj["JCDept"]
      """   The Job Department in which the employee works work was done. An optional field. If entered must be valid in JCDept table.
Used by data collection in the "Work Que" window to provide a default department to view.  """  
      self.SupervisorID:str = obj["SupervisorID"]
      """   The ID of the Supervisor for the employee.  The Supervisor ID is actually the EmpID used for supervisor's PREmpMas record.
Validation: Can't be blank, if entered must be found in the PREmpMas file.  """  
      self.ServTech:bool = obj["ServTech"]
      """  This person usually goes out on service calls  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """   Links the employee to a UserID.  This link is used by the Shop Floor Menu(SFM).  In the SFM, the user signs on with their employee id instead of a User id. This link grants the menu security authorizations of the User to the employee. It also defines the language to be used.
Note: An employee can only be related to one UserFile record. Each UserFile, can be related to many employees.  Therefore, you might set up a few generic Users per language, or based on security levels or you might set up a user for each employee. Note: Many transactions, are stamped with the UserID, thus if you use generic users you will be tracking to the individual employee.
This field is OPTIONAL. However, employee will not be allowed to login to the SFM without a being linked to a UserID.  Also, the company of the employee must be an authorized company of the user. This is validated by the finding a record in UserComp table, using EmpBasic.Company, EmpBasic.DCDUserID.  """  
      self.ShopSupervisor:bool = obj["ShopSupervisor"]
      """  Indicates if this employee is a shop supervisor. This must be checked for employee to use the Shop Floor Menu Supervisor options.  """  
      self.WarehouseManager:bool = obj["WarehouseManager"]
      """  A warehouse manager has the access to the Manager's Queue tab in the Material Request Queue.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Resource Group ID for this employee, only allowed if the Project Billing module licensed.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Resource D for this employee, only allowed if the Project Billing module licensed.  """  
      self.SupervisorName:str = obj["SupervisorName"]
      """  SupervisorName  """  
      self.ShiftDescription:str = obj["ShiftDescription"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ResourceGroupDescription:str = obj["ResourceGroupDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EmpBasicListTableset:
   def __init__(self, obj):
      self.EmpBasicList:list[Erp_Tablesets_EmpBasicListRow] = obj["EmpBasicList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_EmpBasicRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.FirstName:str = obj["FirstName"]
      """  First name of employee.  """  
      self.MiddleInitial:str = obj["MiddleInitial"]
      """  Middle name of employee.  """  
      self.LastName:str = obj["LastName"]
      """  Last name of employee  """  
      self.Name:str = obj["Name"]
      """  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.Address:str = obj["Address"]
      """  First Address Line  """  
      self.Address2:str = obj["Address2"]
      """  Second Address Line  """  
      self.City:str = obj["City"]
      """  City portion of address  """  
      self.State:str = obj["State"]
      """  Home State. Can be blank.  """  
      self.ZIP:str = obj["ZIP"]
      """  Postal Code or Zip code portion of address  """  
      self.Country:str = obj["Country"]
      """  Country is used as part of the mailing address. It can be left blank.  """  
      self.Phone:str = obj["Phone"]
      """  Home phone number  """  
      self.EmgPhone:str = obj["EmgPhone"]
      """  Emergency Phone number  """  
      self.Shift:int = obj["Shift"]
      """  Normal work shift.  Value is to be defaulted from XASyst.DefaultShift (Production/Data Collection tab in Company Configuration) when available, otherwise it is not defaulted.  """  
      self.LaborRate:int = obj["LaborRate"]
      """  Labor rate that is used for Job Costing.  """  
      self.Payroll:bool = obj["Payroll"]
      """   Indicates if this employee is should be paid through the Manufacturing System payroll module.  This does not mean they have been setup in payroll, only that they should be.
Once setup in payroll (existence of corresponding PREmpMas record) this field cannot be changed.  """  
      self.PRSetupReq:bool = obj["PRSetupReq"]
      """  An internally assigned flag that Indicates if the employee needs to be established in payroll. (Existence of PREmpMas). This flag is used to allow payroll employee maintenance view new employees created by job costing that were flagged as being "Payroll" employees.  """  
      self.EmpStatus:str = obj["EmpStatus"]
      """  Indicates the employment status. Can be A-Active, I-InActive or T-Terminated.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """   The default expense code that will be for direct labor hours reported by this employee.  This must be valid in the LabExpCd master file.
This will be used unless labor is reported where the JobHead.ExpenseCode is not blank.  """  
      self.PhotoFile:str = obj["PhotoFile"]
      """  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  """  
      self.JCDept:str = obj["JCDept"]
      """   The Job Department in which the employee works work was done. An optional field. If entered must be valid in JCDept table.
Used by data collection in the "Work Que" window to provide a default department to view.  """  
      self.EmgContact:str = obj["EmgContact"]
      """  Emergency contact name.  """  
      self.SupervisorID:str = obj["SupervisorID"]
      """   The ID of the Supervisor for the employee.  The Supervisor ID is actually the EmpID used for supervisor's PREmpMas record.
Validation: Can't be blank, if entered must be found in the PREmpMas file.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.ServTech:bool = obj["ServTech"]
      """  This person usually goes out on service calls  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Email address of the Employee.  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """   Links the employee to a UserID.  This link is used by the Shop Floor Menu(SFM).  In the SFM, the user signs on with their employee id instead of a User id. This link grants the menu security authorizations of the User to the employee. It also defines the language to be used.
Note: An employee can only be related to one UserFile record. Each UserFile, can be related to many employees.  Therefore, you might set up a few generic Users per language, or based on security levels or you might set up a user for each employee. Note: Many transactions, are stamped with the UserID, thus if you use generic users you will be tracking to the individual employee.
This field is OPTIONAL. However, employee will not be allowed to login to the SFM without a being linked to a UserID.  Also, the company of the employee must be an authorized company of the user. This is validated by the finding a record in UserComp table, using EmpBasic.Company, EmpBasic.DCDUserID.  """  
      self.ProductionWorker:bool = obj["ProductionWorker"]
      """  Indicates if this employee works on the manufacturing line. This must be checked for employee to use the Shop Floor Menu production options.  """  
      self.MaterialHandler:bool = obj["MaterialHandler"]
      """  Indicates if this employee is a material handler. This must be checked for employee to use the Shop Floor Menu material handler options.  """  
      self.ShopSupervisor:bool = obj["ShopSupervisor"]
      """  Indicates if this employee is a shop supervisor. This must be checked for employee to use the Shop Floor Menu Supervisor options.  """  
      self.CanReportQty:bool = obj["CanReportQty"]
      """   Pertains to Data Collection only.
Indicates if the employee is allowed report completed quantities.  """  
      self.CanOverrideJob:bool = obj["CanOverrideJob"]
      """   Pertains to Data Collection only.
Indicates if the job/asm/opr can be overriden when reporting completed quantity.  If NO, then they will only be allowed to report against a job/asm/opr that they are currently working on (active labordtl record ) or where the job is open and the operation is marked as "quantity only" reporting .  If YES, they can enter the quantity for any open job without first having to do a start activity function.
( See also EmpBasic.CanReportQty )  """  
      self.CanRequestMaterial:bool = obj["CanRequestMaterial"]
      """   Pertains to Data Collection/Advanced Material Management only.
Indicates if the employee is allowed make requests for materials.  """  
      self.CanReportScrapQty:bool = obj["CanReportScrapQty"]
      """   Pertains to Data Collection only.
Indicates if the employee is allowed report scrap quantities.  """  
      self.CanReportNCQty:bool = obj["CanReportNCQty"]
      """   Pertains to Data Collection only.
Indicates if the employee is allowed report nonconformance quantities.  """  
      self.ShipRecv:bool = obj["ShipRecv"]
      """  Indicates if this employee is a Shipping/Receiving worker. This must be checked for employee to use the Shop Floor Menu Shipping/Receiving options.  """  
      self.CnvEmpID:str = obj["CnvEmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.WarehouseManager:bool = obj["WarehouseManager"]
      """  A warehouse manager has the access to the Manager's Queue tab in the Material Request Queue.  """  
      self.CanOverrideAllocations:bool = obj["CanOverrideAllocations"]
      """  Employee is able to override a hard allocation against inventory and select it from another Bin during the process of picking and packing orders, as long as it is not allocated to another Sales Order, Job or Transfer Order.  """  
      self.AllowDirLbr:bool = obj["AllowDirLbr"]
      """  If false the shop employee will not be allowed to book time to manufacturing jobs.  """  
      self.ContractEmp:bool = obj["ContractEmp"]
      """  True indicates that the shop employee is on contract rather than paid via the payroll. This flag is then used in the advanced billing invoice preparation process.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Resource Group ID for this employee, only allowed if the Project Billing module licensed.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Resource D for this employee, only allowed if the Project Billing module licensed.  """  
      self.TimeWFGroupID:str = obj["TimeWFGroupID"]
      """  Unique identifier of the workflow group for this employee's Time transactions.  """  
      self.ExpenseEntryAllowed:bool = obj["ExpenseEntryAllowed"]
      """  This value will be true if the Employee is allowed to enter Expense.  """  
      self.ExpenseWFGroupID:str = obj["ExpenseWFGroupID"]
      """  Unique identifier of the workflow group for this employee's Expense transactions.  """  
      self.ExpenseVendorNum:int = obj["ExpenseVendorNum"]
      """  The Supplier Number associated to the Employee for Expense entry.  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.SyncNameToPerCon:bool = obj["SyncNameToPerCon"]
      """  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  """  
      self.SyncAddressToPerCon:bool = obj["SyncAddressToPerCon"]
      """  Default to True. If unchecked then changes to the Address fields on PerCon won't affect this record and visa versa.  """  
      self.SyncPhoneToPerCon:bool = obj["SyncPhoneToPerCon"]
      """  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  """  
      self.SyncEmailToPerCon:bool = obj["SyncEmailToPerCon"]
      """  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  """  
      self.CanEnterIndirectTime:bool = obj["CanEnterIndirectTime"]
      """   Pertains to Time Management.
Maintains whether the employee is allowed to enter Indirect time.  """  
      self.CanEnterProductionTime:bool = obj["CanEnterProductionTime"]
      """   Pertains to Time Management.
Maintains whether the employee is allowed to enter Production time.  """  
      self.CanEnterProjectTime:bool = obj["CanEnterProjectTime"]
      """   Pertains to Time Management.
Maintains whether the employee is allowed to enter Project time.  """  
      self.CanEnterServiceTime:bool = obj["CanEnterServiceTime"]
      """   Pertains to Time Management.
Maintains whether the employee is allowed to enter Service time.  """  
      self.CanEnterSetupTime:bool = obj["CanEnterSetupTime"]
      """   Pertains to Time Management.
Maintains whether the employee is allowed to enter Setup time.  """  
      self.TimeAutoApprove:bool = obj["TimeAutoApprove"]
      """  Time transactions for the employee requiring employee approval logic will automatically be approved.  """  
      self.ExpenseAutoApprove:bool = obj["ExpenseAutoApprove"]
      """  Expense transactions for the employee requiring employee approval logic will automatically be approved.  """  
      self.MobileUserPassword:str = obj["MobileUserPassword"]
      """  Mobile Password  """  
      self.AllowIndirect:bool = obj["AllowIndirect"]
      """  Default is True.  Determines if an employee can enter time with a labor type of Indirect.  If True, an employee may select Indirect labor type.  If false, employee may not select Indirect labor type in Time Entry.  """  
      self.AllowProduction:bool = obj["AllowProduction"]
      """  Default is True.  Determines if an employee can enter time with a labor type of Production.  If True, an employee may select Production labor type.  If false, employee may not select Production labor type in Time Entry.  """  
      self.AllowProject:bool = obj["AllowProject"]
      """  Default is True.  Determines if an employee can enter time with a labor type of Project.  If True, an employee may select Project labor type.  If false, employee may not select Project labor type in Time Entry.  """  
      self.AllowService:bool = obj["AllowService"]
      """  Default is True.  Determines if an employee can enter time with a labor type of Service.  If True, an employee may select Service labor type.  If false, employee may not select Service labor type in Time Entry.  """  
      self.AllowSetup:bool = obj["AllowSetup"]
      """  Default is True.  Determines if an employee can enter time with a labor type of Setup.  If True, an employee may select Setup labor type.  If false, employee may not select Setup labor type in Time Entry.  """  
      self.DefaultLaborTypePseudo:str = obj["DefaultLaborTypePseudo"]
      """   Correlates to LaborType.  Indicates the type of labor transaction, however "Production" LaborType can be broken out into "Project", "Production" or "Service".  Valid Values are "I" = Indirect, "P" - Production, "S" - Setup, "J" - Project, or "V" - Service.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  """  
      self.DefaultTimeTypCd:str = obj["DefaultTimeTypCd"]
      """  Time Type Code  """  
      self.DefaultIndirectCode:str = obj["DefaultIndirectCode"]
      """  A code that links to the Indirect master record that describes the type of indirect labor for this transaction. This field IS DIRECTLY ENTERED, not via a description/selection list method.   This is only valid when LaborType = "I" and must then be valid.  """  
      self.DefaultExpenseCode:str = obj["DefaultExpenseCode"]
      """  The expense code for this labor transaction. An expense code is a abbreviated method of indirectly assigning a G/L account for the labor expense. DEFAULTS: for direct labor;  use the JobHead.ExpenseCode if its non-blank,  else use the Employee.ExpenseCode.                                                                   For Indirect Labor use the Indirect.ExpenseCode if not blank, else use the employee.ExpenseCode.  """  
      self.DefaultResourceGrpID:str = obj["DefaultResourceGrpID"]
      """   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group table.
For production labor (LaborType = "S" or "P") the default is from the JobOper.PrimaryProdDtl JobOpDtl.ResourceGrpID.
For indirect labor (LaborType = I) there is no default.  """  
      self.DefaultResourceID:str = obj["DefaultResourceID"]
      """  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  """  
      self.DefaultLaborHrs:int = obj["DefaultLaborHrs"]
      """  Labor hours are used in calculating labor cost for a job. It is stored as hours-hundredths. It is calculated whenever the start/stop time is changed. It can then be overridden.  """  
      self.DefaultExpCurrencyCode:str = obj["DefaultExpCurrencyCode"]
      """  The currency the expense occurred in.  """  
      self.DefaultClaimCurrencyCode:str = obj["DefaultClaimCurrencyCode"]
      """  The currency the claim amounts are in.  """  
      self.DefaultPMUID:int = obj["DefaultPMUID"]
      """  The payment method of the expense.  """  
      self.DefaultTaxRegionCode:str = obj["DefaultTaxRegionCode"]
      """  The Tax Region for this expense.  """  
      self.DefaultTaxIncluded:bool = obj["DefaultTaxIncluded"]
      """  Indicates if the expense amount includes tax.  """  
      self.ExpenseAdvReqAllowed:bool = obj["ExpenseAdvReqAllowed"]
      """  This value will be true if the Employee is allowed to enter Expense for advance requests.  """  
      self.ExpenseAdvReqWFGroupID:str = obj["ExpenseAdvReqWFGroupID"]
      """  Unique identifier of the workflow group for this employee's Expense advance request transactions.  """  
      self.ExpenseAdvReqAutoApprove:bool = obj["ExpenseAdvReqAutoApprove"]
      """  Advance request expense transactions for the employee requiring employee approval logic will automatically be approved.  """  
      self.MobileResourceID:str = obj["MobileResourceID"]
      """  MobileResourceID  """  
      self.AllowAsAltRemitTo:bool = obj["AllowAsAltRemitTo"]
      """  AllowAsAltRemitTo  """  
      self.UserNameInJDF:str = obj["UserNameInJDF"]
      """  UserNameInJDF  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.PermitScrap:bool = obj["PermitScrap"]
      """  PermitScrap  """  
      self.PermitDown:bool = obj["PermitDown"]
      """  PermitDown  """  
      self.PermitHelp:bool = obj["PermitHelp"]
      """  PermitHelp  """  
      self.PermitJobControl:bool = obj["PermitJobControl"]
      """  PermitJobControl  """  
      self.PermitNextJobControl:bool = obj["PermitNextJobControl"]
      """  PermitNextJobControl  """  
      self.PermitManualSqc:bool = obj["PermitManualSqc"]
      """  PermitManualSqc  """  
      self.PermitVariableSqc:bool = obj["PermitVariableSqc"]
      """  PermitVariableSqc  """  
      self.PermitAttributeSqc:bool = obj["PermitAttributeSqc"]
      """  PermitAttributeSqc  """  
      self.PermitMaterialLot:bool = obj["PermitMaterialLot"]
      """  PermitMaterialLot  """  
      self.PermitSetupMaterial:bool = obj["PermitSetupMaterial"]
      """  PermitSetupMaterial  """  
      self.PermitCavities:bool = obj["PermitCavities"]
      """  PermitCavities  """  
      self.PermitPercentRegrind:bool = obj["PermitPercentRegrind"]
      """  PermitPercentRegrind  """  
      self.PermitSaveProfile:bool = obj["PermitSaveProfile"]
      """  PermitSaveProfile  """  
      self.PermitCalibration:bool = obj["PermitCalibration"]
      """  PermitCalibration  """  
      self.PermitMachinePm:bool = obj["PermitMachinePm"]
      """  PermitMachinePm  """  
      self.PermitToolPm:bool = obj["PermitToolPm"]
      """  PermitToolPm  """  
      self.PermitLanguage:bool = obj["PermitLanguage"]
      """  PermitLanguage  """  
      self.PermitPreferences:bool = obj["PermitPreferences"]
      """  PermitPreferences  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DisallowTimeEntry:bool = obj["DisallowTimeEntry"]
      """  The purpose of the flag is to disallow an employee to enter their own time in Time and Expense Entry  """  
      self.PkgInboundAllowed:bool = obj["PkgInboundAllowed"]
      """  Indicates that an employee can execute inbound related transactions on the shop floor. The default for the check box is unchecked.  """  
      self.PkgOutboundAllowed:bool = obj["PkgOutboundAllowed"]
      """  Indicates that an employee can execute outbound related transactions on the shop floor. The default for the check box is unchecked.  """  
      self.PkgInventoryAllowed:bool = obj["PkgInventoryAllowed"]
      """  Indicates that an employee can execute inventory related transactions on the shop floor. The default for the check box is unchecked.  """  
      self.PkgManufacturingAllowed:bool = obj["PkgManufacturingAllowed"]
      """  Indicates that an employee can execute manufacturing related transactions on the shop floor. The default for the check box is unchecked.  """  
      self.PkgQualityAllowed:bool = obj["PkgQualityAllowed"]
      """  Indicates that an employee can execute quality related transactions on the shop floor. The default for the check box is unchecked.  """  
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.PkgMasterMixedPrint:bool = obj["PkgMasterMixedPrint"]
      """  Package Control Activity setting to indicate if the employee is allowed to print during the Master and MixedMaster.  """  
      self.PkgSuppressPrintMessages:bool = obj["PkgSuppressPrintMessages"]
      """  PkgSuppressPrintMessages  """  
      self.PayrollValuesForHCM:str = obj["PayrollValuesForHCM"]
      """  PayrollValuesForHCM  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the employee has to be synchronized with Epicor FSA application.  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.IDDocument:str = obj["IDDocument"]
      """  Identity Document  """  
      self.BirthDate:str = obj["BirthDate"]
      """  Birthdate  """  
      self.Sex:str = obj["Sex"]
      """  Sex  """  
      self.Department:str = obj["Department"]
      """  Department  """  
      self.EnrollmentDate:str = obj["EnrollmentDate"]
      """  Enrollment Date  """  
      self.DepartureDate:str = obj["DepartureDate"]
      """  Departure Date  """  
      self.AlertFlag:bool = obj["AlertFlag"]
      """  Should this employee receive email alert messages.  """  
      self.DepartmentDescription:str = obj["DepartmentDescription"]
      """  Department Description  """  
      self.EnableExpenseSupplier:bool = obj["EnableExpenseSupplier"]
      """  external field for UI to use to know whether it should enable or disable the ExpenseVendorNumVendorID field.  """  
      self.ExpenseDescription:str = obj["ExpenseDescription"]
      """  Expense Description  """  
      self.ExpenseDisableCreate:bool = obj["ExpenseDisableCreate"]
      """  Indicates whether the user is allowed to create Expense transactions in Time and Expense Entry for another employee for which they are an Approver.  """  
      self.ExpenseRestrictEntry:bool = obj["ExpenseRestrictEntry"]
      self.FoundPayroll:bool = obj["FoundPayroll"]
      """  Payroll record has been found so changes to many fields are disallowed.  """  
      self.FoundPayrollUserAllowed:bool = obj["FoundPayrollUserAllowed"]
      """  Payroll record has been found so changes to many fields are disallowed, but the user is in the employee's payroll class so can see the labor rate field  """  
      self.HCMEnabledAt:str = obj["HCMEnabledAt"]
      """  String value which contains the validations for the HCM Integration, possible values NON(Nothing configured), HDR (Header) DTL (Detail)  """  
      self.IsHCMAllowedByEmp:bool = obj["IsHCMAllowedByEmp"]
      """  External field used on Employee Entry in order to enable/disable HCM configuration  """  
      self.PayrollValuesForHCMDsp:str = obj["PayrollValuesForHCMDsp"]
      """  Displays blank if "Allow Override Integrate Labor Pay Hours at Employee" checkbox in Site configuration is unchecked and Employee's value if checked.  """  
      self.PerConName:str = obj["PerConName"]
      self.PhotoFilePath:str = obj["PhotoFilePath"]
      """  Path to the photo file if it exists.  """  
      self.SetShopLoad:bool = obj["SetShopLoad"]
      """  Flag used to indicate that the generate fill shop capacity process needs to be run to update the ShopCap records because new records won't be added due performance.  """  
      self.ShiftEndTime:str = obj["ShiftEndTime"]
      """  Shift end time in Hours:Minute format., used by Shop Tracker  """  
      self.ShiftStartTime:str = obj["ShiftStartTime"]
      """  Shift start time in Hours:Minutes format  """  
      self.SupervisorName:str = obj["SupervisorName"]
      """  SupervisorName  """  
      self.TimeDisableCreate:bool = obj["TimeDisableCreate"]
      """  Indicates whether the user is allowed to create a Time transaction in Time and Expense Entry for another employee for which they are an Approver.  """  
      self.TimeRestrictEntry:bool = obj["TimeRestrictEntry"]
      self.UserIDName:str = obj["UserIDName"]
      """  User ID Name  """  
      self.CalendarID:str = obj["CalendarID"]
      self.COASegReferences:str = obj["COASegReferences"]
      """  List of fields which are referenced by COA segments.  """  
      self.TimeApprovalTasksTree:str = obj["TimeApprovalTasksTree"]
      """  This column used to display Time Approval Task tree in MetaUI  """  
      self.ExpenseApprovalTasksTree:str = obj["ExpenseApprovalTasksTree"]
      """  This column used to display Time Approval Task tree in MetaUI  """  
      self.ShiftLength:int = obj["ShiftLength"]
      self.BitFlag:int = obj["BitFlag"]
      self.CompanySendToFSA:bool = obj["CompanySendToFSA"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.ExpenseCodeDescription:str = obj["ExpenseCodeDescription"]
      self.ExpenseVendorNumName:str = obj["ExpenseVendorNumName"]
      self.ExpenseVendorNumCity:str = obj["ExpenseVendorNumCity"]
      self.ExpenseVendorNumTermsCode:str = obj["ExpenseVendorNumTermsCode"]
      self.ExpenseVendorNumAddress3:str = obj["ExpenseVendorNumAddress3"]
      self.ExpenseVendorNumDefaultFOB:str = obj["ExpenseVendorNumDefaultFOB"]
      self.ExpenseVendorNumCurrencyCode:str = obj["ExpenseVendorNumCurrencyCode"]
      self.ExpenseVendorNumZIP:str = obj["ExpenseVendorNumZIP"]
      self.ExpenseVendorNumVendorID:str = obj["ExpenseVendorNumVendorID"]
      self.ExpenseVendorNumAddress2:str = obj["ExpenseVendorNumAddress2"]
      self.ExpenseVendorNumAddress1:str = obj["ExpenseVendorNumAddress1"]
      self.ExpenseVendorNumCountry:str = obj["ExpenseVendorNumCountry"]
      self.ExpenseVendorNumState:str = obj["ExpenseVendorNumState"]
      self.JCDeptDescription:str = obj["JCDeptDescription"]
      self.MachineDescription:str = obj["MachineDescription"]
      self.ResourceDescription:str = obj["ResourceDescription"]
      self.ResourceGroupDescription:str = obj["ResourceGroupDescription"]
      self.ShiftDescription:str = obj["ShiftDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EmpBasicTableset:
   def __init__(self, obj):
      self.EmpBasic:list[Erp_Tablesets_EmpBasicRow] = obj["EmpBasic"]
      self.EmpBasicAttch:list[Erp_Tablesets_EmpBasicAttchRow] = obj["EmpBasicAttch"]
      self.EmpLabExpRate:list[Erp_Tablesets_EmpLabExpRateRow] = obj["EmpLabExpRate"]
      self.EmpCal:list[Erp_Tablesets_EmpCalRow] = obj["EmpCal"]
      self.Partner:list[Erp_Tablesets_PartnerRow] = obj["Partner"]
      self.ResourceCal:list[Erp_Tablesets_ResourceCalRow] = obj["ResourceCal"]
      self.EmpRole:list[Erp_Tablesets_EmpRoleRow] = obj["EmpRole"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.EmpRoleRt:list[Erp_Tablesets_EmpRoleRtRow] = obj["EmpRoleRt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_EmpCalRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.CalendarID:str = obj["CalendarID"]
      """  Epmloyee Calendar ID  """  
      self.FromEffectiveDate:str = obj["FromEffectiveDate"]
      """  From Effective Date of this Calendar for this Employee.  The value must be unique per Company/Employee/Calendar.  This value cannot be changed after the initial save.  """  
      self.ToEffectiveDate:str = obj["ToEffectiveDate"]
      """  To Effective Date of this Calendar for this Employee.  Value is not required.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CalendarIDDescription:str = obj["CalendarIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EmpLabExpRateRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.EmpID:str = obj["EmpID"]
      """  EmpID  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode  """  
      self.RateType:int = obj["RateType"]
      """  RateType  """  
      self.RateMultiplier:int = obj["RateMultiplier"]
      """  RateMultiplier  """  
      self.FixedRate:int = obj["FixedRate"]
      """  FixedRate  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.EmpBasicName:str = obj["EmpBasicName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EmpRoleRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RoleCd:str = obj["RoleCd"]
      """  Project Role Code  """  
      self.Primary:bool = obj["Primary"]
      """  Setting this to true defines this role code as the  primary Project Role for the employee.ONLY one role code can be defined as primary.  """  
      self.TimeApprover:bool = obj["TimeApprover"]
      """  Determines if this Employee is a Time Approver through this Role.  """  
      self.ExpenseApprover:bool = obj["ExpenseApprover"]
      """  Determines if this Employee is a Expense Approver through this Role.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.EmpBasicName:str = obj["EmpBasicName"]
      self.EmpBasicFirstName:str = obj["EmpBasicFirstName"]
      self.EmpBasicLastName:str = obj["EmpBasicLastName"]
      self.RoleCdRoleDescription:str = obj["RoleCdRoleDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EmpRoleRtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RoleCd:str = obj["RoleCd"]
      """  Project Role Code  """  
      self.RateEffDte:str = obj["RateEffDte"]
      """  The effective date of the project role code rate.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.TimeTypCd:str = obj["TimeTypCd"]
      """  Time Type Code  """  
      self.Rate:int = obj["Rate"]
      """  The charge rate for project role code expressed in the designated currency code.  """  
      self.RateEndDte:str = obj["RateEndDte"]
      """  The end date of the project role code rate.  """  
      self.Seq:int = obj["Seq"]
      """  Sequence field used to keep the primary key unique  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.EmpBasicFirstName:str = obj["EmpBasicFirstName"]
      self.EmpBasicName:str = obj["EmpBasicName"]
      self.EmpBasicLastName:str = obj["EmpBasicLastName"]
      self.RoleCdRoleDescription:str = obj["RoleCdRoleDescription"]
      self.TimeTypCdDescription:str = obj["TimeTypCdDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Identifier of the GL Control Type.  """  
      self.GLControlCode:str = obj["GLControlCode"]
      """  GL Control Identifier.  """  
      self.BusinessEntity:str = obj["BusinessEntity"]
      """  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.GlobalEntityGLC:bool = obj["GlobalEntityGLC"]
      """  Marks this EntityGLC as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the related BankAcct record.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      self.CallCode:str = obj["CallCode"]
      """  CallCode of the related FSCallCd record.  """  
      self.ChargeCode:str = obj["ChargeCode"]
      self.ClassCode:str = obj["ClassCode"]
      """  ClassCode of the related FAClass record.  """  
      self.ClassID:str = obj["ClassID"]
      """  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  """  
      self.ContractCode:str = obj["ContractCode"]
      """  ContractCode of the related FSContCd record.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode of the related Currency record.  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum of the related Customer record  """  
      self.DeductionID:str = obj["DeductionID"]
      """  DeductionID of PRClsDed or PRDeduct.  """  
      self.EmpID:str = obj["EmpID"]
      """  EmpID of the related PREmpMas record.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode of PayTLbr, LabExpCd  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID of ExtCompany table  """  
      self.FromPlant:str = obj["FromPlant"]
      """  FromPlant value of the related PlntTranDef record.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  GroupCode of the related FAGroup record.  """  
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.JCDept:str = obj["JCDept"]
      """  JCDept of the related JCDept record.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  MiscCode of the related MiscChrg or PurMisc record.  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum of the related Part record.  """  
      self.PayTypeID:str = obj["PayTypeID"]
      """  PayTypeID of PayType  """  
      self.PerConName:str = obj["PerConName"]
      self.PIStatus:str = obj["PIStatus"]
      """  PI Status  """  
      self.Plant:str = obj["Plant"]
      """  Plant of the related PlantConfCtrl record.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdCode of the related ProdGrup record.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID of the related Project record.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  PurchCode of the related GLPurch record.  """  
      self.RateCode:str = obj["RateCode"]
      """  RateCode of the related GLRate record.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  ReasonCode of the related Reason record.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  ReasonType of the related Reason record.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  SalesCatID of the related SalesCat record.  """  
      self.Shift:int = obj["Shift"]
      """  Shift value of the related JCShift record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode of the related SalesTax record.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  TaxTblID of PRTaxMas or PRClsTax.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  ToPlant value of the related PlntTranDef record.  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  TransferMethod of ExtCompany table  """  
      self.TypeID:str = obj["TypeID"]
      """  Type ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum of the related Vendor record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  WarehouseCode of the related Warehse record.  """  
      self.ExpenseTypeCode:str = obj["ExpenseTypeCode"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.OprTypeCode:str = obj["OprTypeCode"]
      self.CashDeskID:str = obj["CashDeskID"]
      self.TIN:str = obj["TIN"]
      self.ReclassCodeID:str = obj["ReclassCodeID"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartnerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PartnerNum:int = obj["PartnerNum"]
      """  PartnerNum  """  
      self.PartnerType:int = obj["PartnerType"]
      """  PartnerType  """  
      self.SearchID:str = obj["SearchID"]
      """  SearchID  """  
      self.IsActive:bool = obj["IsActive"]
      """  IsActive  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.PartnerID:str = obj["PartnerID"]
      """  PartnerID  """  
      self.DspSearchID:str = obj["DspSearchID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ResourceCalRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  A code uniquely identifies a Resource Group.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource.  """  
      self.SpecialDay:str = obj["SpecialDay"]
      """  Exception Day  """  
      self.ProdHour01:bool = obj["ProdHour01"]
      """  ProdHour01  """  
      self.ProdHour02:bool = obj["ProdHour02"]
      """  ProdHour02  """  
      self.ProdHour03:bool = obj["ProdHour03"]
      """  ProdHour03  """  
      self.ProdHour04:bool = obj["ProdHour04"]
      """  ProdHour04  """  
      self.ProdHour05:bool = obj["ProdHour05"]
      """  ProdHour05  """  
      self.ProdHour06:bool = obj["ProdHour06"]
      """  ProdHour06  """  
      self.ProdHour07:bool = obj["ProdHour07"]
      """  ProdHour07  """  
      self.ProdHour08:bool = obj["ProdHour08"]
      """  ProdHour08  """  
      self.ProdHour09:bool = obj["ProdHour09"]
      """  ProdHour09  """  
      self.ProdHour10:bool = obj["ProdHour10"]
      """  ProdHour10  """  
      self.ProdHour11:bool = obj["ProdHour11"]
      """  ProdHour11  """  
      self.ProdHour12:bool = obj["ProdHour12"]
      """  ProdHour12  """  
      self.ProdHour13:bool = obj["ProdHour13"]
      """  ProdHour13  """  
      self.ProdHour14:bool = obj["ProdHour14"]
      """  ProdHour14  """  
      self.ProdHour15:bool = obj["ProdHour15"]
      """  ProdHour15  """  
      self.ProdHour16:bool = obj["ProdHour16"]
      """  ProdHour16  """  
      self.ProdHour17:bool = obj["ProdHour17"]
      """  ProdHour17  """  
      self.ProdHour18:bool = obj["ProdHour18"]
      """  ProdHour18  """  
      self.ProdHour19:bool = obj["ProdHour19"]
      """  ProdHour19  """  
      self.ProdHour20:bool = obj["ProdHour20"]
      """  ProdHour20  """  
      self.ProdHour21:bool = obj["ProdHour21"]
      """  ProdHour21  """  
      self.ProdHour22:bool = obj["ProdHour22"]
      """  ProdHour22  """  
      self.ProdHour23:bool = obj["ProdHour23"]
      """  ProdHour23  """  
      self.ProdHour24:bool = obj["ProdHour24"]
      """  ProdHour24  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExceptionLabel:str = obj["ExceptionLabel"]
      """  ExceptionLabel  """  
      self.DispExceptionLabel:str = obj["DispExceptionLabel"]
      """  Display Exception Label  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtEmpBasicTableset:
   def __init__(self, obj):
      self.EmpBasic:list[Erp_Tablesets_EmpBasicRow] = obj["EmpBasic"]
      self.EmpBasicAttch:list[Erp_Tablesets_EmpBasicAttchRow] = obj["EmpBasicAttch"]
      self.EmpLabExpRate:list[Erp_Tablesets_EmpLabExpRateRow] = obj["EmpLabExpRate"]
      self.EmpCal:list[Erp_Tablesets_EmpCalRow] = obj["EmpCal"]
      self.Partner:list[Erp_Tablesets_PartnerRow] = obj["Partner"]
      self.ResourceCal:list[Erp_Tablesets_ResourceCalRow] = obj["ResourceCal"]
      self.EmpRole:list[Erp_Tablesets_EmpRoleRow] = obj["EmpRole"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.EmpRoleRt:list[Erp_Tablesets_EmpRoleRtRow] = obj["EmpRoleRt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class FromEffDateOverlaps_input:
   """ Required : 
   employeeID
   effDate
   """  
   def __init__(self, obj):
      self.employeeID:str = obj["employeeID"]
      self.effDate:str = obj["effDate"]
      pass

class FromEffDateOverlaps_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class GetByIDForExpense_input:
   """ Required : 
   inEmpID
   """  
   def __init__(self, obj):
      self.inEmpID:str = obj["inEmpID"]
      pass

class GetByIDForExpense_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EmpBasicTableset] = obj["returnObj"]
      pass

class GetByIDForTE_input:
   """ Required : 
   inEmpID
   """  
   def __init__(self, obj):
      self.inEmpID:str = obj["inEmpID"]
      pass

class GetByIDForTE_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EmpBasicTableset] = obj["returnObj"]
      pass

class GetByIDForTime_input:
   """ Required : 
   inEmpID
   """  
   def __init__(self, obj):
      self.inEmpID:str = obj["inEmpID"]
      pass

class GetByIDForTime_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EmpBasicTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   empID
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EmpBasicTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_EmpBasicTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_EmpBasicTableset] = obj["returnObj"]
      pass

class GetClientFileName_input:
   """ Required : 
   IP_ServerFileName
   """  
   def __init__(self, obj):
      self.IP_ServerFileName:str = obj["IP_ServerFileName"]
      pass

class GetClientFileName_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetDefaultEmpID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.defaultEmpID:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetEmpStatusCodeDescList_input:
   """ Required : 
   TableName
   FieldName
   FoundPayroll
   """  
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.FieldName:str = obj["FieldName"]
      self.FoundPayroll:bool = obj["FoundPayroll"]
      pass

class GetEmpStatusCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetIfCurrentSiteHasExternalMES_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class GetListExpEmployees_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Whereclause for EmpBasic table.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetListExpEmployees_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EmpBasicListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListForExpense_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Whereclause for EmpBasic table.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetListForExpense_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EmpBasicListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListForTE_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Whereclause for EmpBasic table.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetListForTE_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EmpBasicListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListForTime_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Whereclause for EmpBasic table.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetListForTime_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EmpBasicListTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_EmpBasicListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewEmpBasicAttch_input:
   """ Required : 
   ds
   empID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      self.empID:str = obj["empID"]
      pass

class GetNewEmpBasicAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewEmpBasic_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

class GetNewEmpBasic_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewEmpCal_input:
   """ Required : 
   ds
   empID
   calendarID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      self.empID:str = obj["empID"]
      self.calendarID:str = obj["calendarID"]
      pass

class GetNewEmpCal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewEmpLabExpRate_input:
   """ Required : 
   ds
   empID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      self.empID:str = obj["empID"]
      pass

class GetNewEmpLabExpRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewEmpRoleRt_input:
   """ Required : 
   ds
   empID
   roleCd
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      self.empID:str = obj["empID"]
      self.roleCd:str = obj["roleCd"]
      pass

class GetNewEmpRoleRt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewEmpRole_input:
   """ Required : 
   ds
   empID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      self.empID:str = obj["empID"]
      pass

class GetNewEmpRole_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewEntityGLC_input:
   """ Required : 
   ds
   relatedToFile
   key1
   key2
   key3
   key4
   key5
   key6
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.key6:str = obj["key6"]
      pass

class GetNewEntityGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPartner_input:
   """ Required : 
   ds
   partnerNum
   partnerType
   partnerID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      self.partnerNum:int = obj["partnerNum"]
      self.partnerType:int = obj["partnerType"]
      self.partnerID:str = obj["partnerID"]
      pass

class GetNewPartner_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewResourceCal_input:
   """ Required : 
   ds
   resourceGrpID
   resourceID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      self.resourceGrpID:str = obj["resourceGrpID"]
      self.resourceID:str = obj["resourceID"]
      pass

class GetNewResourceCal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPerConData_input:
   """ Required : 
   PerConID
   ds
   """  
   def __init__(self, obj):
      self.PerConID:int = obj["PerConID"]
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

class GetPerConData_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsFromList_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicListTableset] = obj["ds"]
      pass

class GetRowsFromList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EmpBasicTableset] = obj["returnObj"]
      pass

class GetRowsWhoIsNotHere_input:
   """ Required : 
   whereClauseEmpBasic
   whereClauseEmpBasicAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseEmpBasic:str = obj["whereClauseEmpBasic"]
      """  Whereclause for EmpBasic table.  """  
      self.whereClauseEmpBasicAttch:str = obj["whereClauseEmpBasicAttch"]
      """  Whereclause for EmpBasicAttch table.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsWhoIsNotHere_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EmpBasicTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseEmpBasic
   whereClauseEmpBasicAttch
   whereClauseEmpLabExpRate
   whereClauseEmpCal
   whereClausePartner
   whereClauseResourceCal
   whereClauseEmpRole
   whereClauseEntityGLC
   whereClauseEmpRoleRt
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseEmpBasic:str = obj["whereClauseEmpBasic"]
      self.whereClauseEmpBasicAttch:str = obj["whereClauseEmpBasicAttch"]
      self.whereClauseEmpLabExpRate:str = obj["whereClauseEmpLabExpRate"]
      self.whereClauseEmpCal:str = obj["whereClauseEmpCal"]
      self.whereClausePartner:str = obj["whereClausePartner"]
      self.whereClauseResourceCal:str = obj["whereClauseResourceCal"]
      self.whereClauseEmpRole:str = obj["whereClauseEmpRole"]
      self.whereClauseEntityGLC:str = obj["whereClauseEntityGLC"]
      self.whereClauseEmpRoleRt:str = obj["whereClauseEmpRoleRt"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EmpBasicTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Hours2Int_input:
   """ Required : 
   vTime
   """  
   def __init__(self, obj):
      self.vTime:str = obj["vTime"]
      pass

class Hours2Int_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
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

class Mins2Int_input:
   """ Required : 
   vTime
   """  
   def __init__(self, obj):
      self.vTime:str = obj["vTime"]
      pass

class Mins2Int_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

class ModifySearchIDs_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

class ModifySearchIDs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeCalendarID_input:
   """ Required : 
   ipCalendarID
   ds
   """  
   def __init__(self, obj):
      self.ipCalendarID:str = obj["ipCalendarID"]
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

class OnChangeCalendarID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeCurrencyCode_input:
   """ Required : 
   ipCurrencyCode
   ds
   """  
   def __init__(self, obj):
      self.ipCurrencyCode:str = obj["ipCurrencyCode"]
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

class OnChangeCurrencyCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeExpenseAllowed_input:
   """ Required : 
   allowExpenses
   ds
   """  
   def __init__(self, obj):
      self.allowExpenses:bool = obj["allowExpenses"]
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

class OnChangeExpenseAllowed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeExpenseAutoApprove_input:
   """ Required : 
   proposedExpenseAutoApprove
   ds
   """  
   def __init__(self, obj):
      self.proposedExpenseAutoApprove:bool = obj["proposedExpenseAutoApprove"]
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

class OnChangeExpenseAutoApprove_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeExpenseVendor_input:
   """ Required : 
   ipVendorID
   ds
   """  
   def __init__(self, obj):
      self.ipVendorID:str = obj["ipVendorID"]
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

class OnChangeExpenseVendor_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeRateEffectiveDate_input:
   """ Required : 
   ipEffRate
   ds
   """  
   def __init__(self, obj):
      self.ipEffRate:str = obj["ipEffRate"]
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

class OnChangeRateEffectiveDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeRateEndDate_input:
   """ Required : 
   ipEndRate
   ds
   """  
   def __init__(self, obj):
      self.ipEndRate:str = obj["ipEndRate"]
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

class OnChangeRateEndDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeResourceGrp_input:
   """ Required : 
   ipResourceGrp
   ds
   """  
   def __init__(self, obj):
      self.ipResourceGrp:str = obj["ipResourceGrp"]
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

class OnChangeResourceGrp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.resourceMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeResource_input:
   """ Required : 
   ipResource
   ds
   """  
   def __init__(self, obj):
      self.ipResource:str = obj["ipResource"]
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

class OnChangeResource_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.resourceMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeRoleCd_input:
   """ Required : 
   ipRoleCd
   ds
   """  
   def __init__(self, obj):
      self.ipRoleCd:str = obj["ipRoleCd"]
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

class OnChangeRoleCd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTimeAutoApprove_input:
   """ Required : 
   proposedTimeAutoApprove
   ds
   """  
   def __init__(self, obj):
      self.proposedTimeAutoApprove:bool = obj["proposedTimeAutoApprove"]
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

class OnChangeTimeAutoApprove_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTimeTypeCode_input:
   """ Required : 
   ipTimeTypeCd
   ds
   """  
   def __init__(self, obj):
      self.ipTimeTypeCd:str = obj["ipTimeTypeCd"]
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

class OnChangeTimeTypeCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeWFGroup_input:
   """ Required : 
   ipColChanging
   ipWFGrpID
   ds
   """  
   def __init__(self, obj):
      self.ipColChanging:str = obj["ipColChanging"]
      """  The column name changing  """  
      self.ipWFGrpID:str = obj["ipWFGrpID"]
      """  The value changing  """  
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

class OnChangeWFGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtEmpBasicTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtEmpBasicTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateResourceCal_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

class UpdateResourceCal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpBasicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class getValidCompanyName_input:
   """ Required : 
   proposedCompany
   """  
   def __init__(self, obj):
      self.proposedCompany:str = obj["proposedCompany"]
      pass

class getValidCompanyName_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

